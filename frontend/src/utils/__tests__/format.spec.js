import { describe, it, expect } from 'vitest'
import { formatPrice } from '../format'

describe('formatPrice', () => {
  it('แสดงสกุลเงินบาทพร้อมคั่นหลักพัน', () => {
    expect(formatPrice(1890)).toBe('฿1,890.00')
  })

  it('รับค่าที่เป็น String ได้', () => {
    expect(formatPrice('250.5')).toBe('฿250.50')
  })
})