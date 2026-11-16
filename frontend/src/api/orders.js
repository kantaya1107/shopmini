import http from './http'

export const orderApi = {
  create: (items) => http.post('/orders', { items }).then((r) => r.data),
  mine: () => http.get('/orders/me').then((r) => r.data),
}