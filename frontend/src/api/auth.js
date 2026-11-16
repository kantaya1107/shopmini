import http from './http'

export const authApi = {
  // OAuth2PasswordRequestForm ต้องการข้อมูลแบบ Form (application/x-www-form-urlencoded)
  login: (email, password) =>
    http
      .post('/auth/login', new URLSearchParams({ username: email, password }))
      .then((r) => r.data),
  register: (payload) => http.post('/auth/register', payload).then((r) => r.data),
  me: () => http.get('/auth/me').then((r) => r.data),
}