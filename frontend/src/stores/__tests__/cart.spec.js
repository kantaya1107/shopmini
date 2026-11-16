import { describe, it, expect, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'
import { nextTick } from 'vue'
import { useCartStore } from '../cart'

const mouse = { id: 1, name: 'เมาส์', price: 590, stock: 3, image_url: '' }
const cable = { id: 8, name: 'สาย USB-C', price: 250, stock: 60, image_url: '' }

describe('Cart Store', () => {
  beforeEach(() => {
    localStorage.clear()
    setActivePinia(createPinia()) // Store ใหม่ทุกเทส ไม่มีสถานะค้างจากเทสก่อน
  })

  it('เพิ่มสินค้าใหม่ และรวมจำนวนเมื่อเพิ่มสินค้าเดิมซ้ำ', () => {
    const cart = useCartStore()
    cart.addItem(mouse)
    cart.addItem(mouse)
    cart.addItem(cable, 3)

    expect(cart.items).toHaveLength(2)
    expect(cart.totalItems).toBe(5)
    expect(cart.totalPrice).toBe(590 * 2 + 250 * 3)
  })

  it('ไม่ให้จำนวนเกินสต็อก', () => {
    const cart = useCartStore()
    cart.addItem(mouse, 10)
    cart.increase(1)

    expect(cart.items[0].qty).toBe(3)
  })

  it('ไม่เพิ่มสินค้าที่หมดสต็อก', () => {
    const cart = useCartStore()
    cart.addItem({ ...mouse, stock: 0 })
    expect(cart.isEmpty).toBe(true)
  })

  it('ลดจำนวนจนเหลือ 0 แล้วลบออกจากตะกร้า', () => {
    const cart = useCartStore()
    cart.addItem(cable)
    cart.decrease(8)
    expect(cart.isEmpty).toBe(true)
  })

  it('บันทึกตะกร้าลง localStorage และโหลดกลับมาได้', async () => {
    const cart = useCartStore()
    cart.addItem(cable, 2)
    await nextTick() // รอให้ watch ทำงาน

    const saved = JSON.parse(localStorage.getItem('shopmini-cart'))
    expect(saved[0]).toMatchObject({ id: 8, qty: 2 })

    setActivePinia(createPinia()) // จำลองการรีเฟรชหน้า
    expect(useCartStore().totalItems).toBe(2)
  })
})