const priceFormatter = new Intl.NumberFormat('th-TH', { style: 'currency', currency: 'THB' })

export const formatPrice = (value) => priceFormatter.format(Number(value))

export const formatDate = (value) =>
  new Intl.DateTimeFormat('th-TH', { dateStyle: 'medium', timeStyle: 'short' }).format(new Date(value))