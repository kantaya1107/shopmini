import http from './http'

export const productApi = {
  list: (params) => http.get('/products', { params }).then((r) => r.data),
  get: (id) => http.get(`/products/${id}`).then((r) => r.data),
  create: (payload) => http.post('/products', payload).then((r) => r.data),
  update: (id, payload) => http.patch(`/products/${id}`, payload).then((r) => r.data),
  remove: (id) => http.delete(`/products/${id}`),
  categories: () => http.get('/categories').then((r) => r.data),
}