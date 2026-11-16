import { describe, it, expect, beforeEach, vi } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { useAuthStore } from '../auth'
import { authApi } from '@/api/auth'

// Mock ทั้งโมดูล api/auth: เทสไม่ยิง HTTP จริง จึงเร็วและไม่ขึ้นกับ Backend
vi.mock('@/api/auth', () => ({
  authApi: {
    login: vi.fn(),
    register: vi.fn(),
    me: vi.fn(),
  },
}))

describe('Auth Store', () => {
  beforeEach(() => {
    localStorage.clear()
    vi.clearAllMocks()
    setActivePinia(createPinia())
  })

  it('login สำเร็จ: เก็บ Token และข้อมูลผู้ใช้', async () => {
    authApi.login.mockResolvedValue({ access_token: 'fake-jwt', token_type: 'bearer' })
    authApi.me.mockResolvedValue({ id: 1, full_name: 'ผู้ดูแล', role: 'admin' })
    const auth = useAuthStore()

    await auth.login('admin@example.com', 'Admin@1234')

    expect(authApi.login).toHaveBeenCalledWith('admin@example.com', 'Admin@1234')
    expect(auth.token).toBe('fake-jwt')
    expect(localStorage.getItem('shopmini-token')).toBe('fake-jwt')
    expect(auth.isAuthenticated).toBe(true)
    expect(auth.isAdmin).toBe(true)
  })

  it('login ไม่สำเร็จ: ไม่เก็บ Token และโยน Error ต่อให้หน้าจอจัดการ', async () => {
    authApi.login.mockRejectedValue(new Error('401'))
    const auth = useAuthStore()

    await expect(auth.login('a@example.com', 'wrong')).rejects.toThrow('401')
    expect(auth.isAuthenticated).toBe(false)
    expect(authApi.me).not.toHaveBeenCalled()
  })

  it('logout ล้างทั้ง State และ localStorage', () => {
    localStorage.setItem('shopmini-token', 'old')
    const auth = useAuthStore()

    auth.logout()

    expect(auth.token).toBeNull()
    expect(localStorage.getItem('shopmini-token')).toBeNull()
  })
})