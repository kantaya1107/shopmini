import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/auth'

const TOKEN_KEY = 'shopmini-token'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem(TOKEN_KEY))
  const user = ref(null)

  const isAuthenticated = computed(() => Boolean(token.value))
  const isAdmin = computed(() => user.value?.role === 'admin')

  function setToken(value) {
    token.value = value
    if (value) localStorage.setItem(TOKEN_KEY, value)
    else localStorage.removeItem(TOKEN_KEY)
  }

  async function login(email, password) {
    const data = await authApi.login(email, password)
    setToken(data.access_token)
    await fetchMe()
  }

  async function register(payload) {
    await authApi.register(payload)
    await login(payload.email, payload.password)
  }

  async function fetchMe() {
    user.value = await authApi.me()
    return user.value
  }

  function logout() {
    setToken(null)
    user.value = null
  }

  return { token, user, isAuthenticated, isAdmin, login, register, fetchMe, logout }
})