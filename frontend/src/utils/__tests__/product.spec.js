import { describe, it, expect } from 'vitest'
import { filterProducts } from '../product'

const products = [
  { id: 1, name: 'เมาส์ไร้สาย', category: { slug: 'accessories' } },
  { id: 2, name: 'หูฟังบลูทูธ ANC', category: { slug: 'audio' } },
  { id: 3, name: 'USB-C Hub', category: { slug: 'accessories' } },
]

describe('filterProducts', () => {
  it('คืนสินค้าทั้งหมดเมื่อไม่มีตัวกรอง', () => {
    expect(filterProducts(products)).toHaveLength(3)
  })

  it('ค้นหาโดยไม่สนตัวพิมพ์เล็กใหญ่', () => {
    const result = filterProducts(products, 'usb')
    expect(result.map((p) => p.id)).toEqual([3])
  })

  it('กรองตามหมวดหมู่ร่วมกับคำค้นหา', () => {
    const result = filterProducts(products, 'เมาส์', 'accessories')
    expect(result.map((p) => p.id)).toEqual([1])
  })

  it('ไม่แก้ไข Array ต้นฉบับ', () => {
    filterProducts(products, 'x')
    expect(products).toHaveLength(3)
  })
})