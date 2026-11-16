import axios from 'axios'
import router from '@/router'
import { useAuthStore } from '@/stores/auth'

// Instance กลาง: รวม baseURL, timeout และ Interceptor ไว้ที่เดียว
const http = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
})

// Request Interceptor: แนบ Token ให้ทุก Request อัตโนมัติ
http.interceptors.request.use((config) => {
  const auth = useAuthStore()
  if (auth.token) {
    config.headers.Authorization = `Bearer ${auth.token}`
  }
  return config
})

// Response Interceptor: จัดการ Error แบบรวมศูนย์
http.interceptors.response.use(
  (response) => response,
  (error) => {
    const status = error.response?.status
    const isLoginRequest = error.config?.url?.includes('/auth/login')

    if (status === 401 && !isLoginRequest) {
      const auth = useAuthStore()
      auth.logout()
      // พากลับหน้าเข้าสู่ระบบ เฉพาะเมื่ออยู่ในหน้าที่ต้องยืนยันตัวตน
      const current = router.currentRoute.value
      if (current.meta.requiresAuth) {
        router.push({ name: 'login', query: { redirect: current.fullPath, expired: '1' } })
      }
    }
    return Promise.reject(error)
  },
)

// แปลง Error ทุกรูปแบบให้เป็นข้อความที่แสดงผู้ใช้ได้
export function getErrorMessage(error) {
  if (error.response?.data?.error?.message) return error.response.data.error.message
  if (error.code === 'ECONNABORTED') return 'เซิร์ฟเวอร์ตอบสนองช้าเกินไป กรุณาลองใหม่'
  if (!error.response) return 'เชื่อมต่อเซิร์ฟเวอร์ไม่ได้ กรุณาตรวจสอบอินเทอร์เน็ต'
  return 'เกิดข้อผิดพลาด กรุณาลองใหม่'
}

export default http