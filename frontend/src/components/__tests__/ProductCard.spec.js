import { describe, it, expect } from 'vitest'
import { mount, RouterLinkStub } from '@vue/test-utils'
import ProductCard from '../ProductCard.vue'

const product = {
  id: 5,
  name: 'หูฟังบลูทูธ ANC',
  price: 2490,
  stock: 10,
  image_url: 'https://example.com/a.jpg',
  category: { id: 2, name: 'เครื่องเสียง', slug: 'audio' },
}

// RouterLinkStub แทน <RouterLink> จริง เพื่อไม่ต้องสร้าง Router ทั้งระบบในเทส
const mountCard = (props) =>
  mount(ProductCard, { props, global: { stubs: { RouterLink: RouterLinkStub } } })

describe('ProductCard', () => {
  it('แสดงชื่อ ราคา และหมวดหมู่ตาม Props', () => {
    const wrapper = mountCard({ product })

    expect(wrapper.get('[data-test="product-name"]').text()).toBe('หูฟังบลูทูธ ANC')
    expect(wrapper.get('[data-test="product-price"]').text()).toBe('฿2,490.00')
    expect(wrapper.text()).toContain('เครื่องเสียง')
  })

  it('ส่ง Event add-to-cart พร้อมข้อมูลสินค้าเมื่อกดปุ่ม', async () => {
    const wrapper = mountCard({ product })

    await wrapper.get('[data-test="add-to-cart"]').trigger('click')

    expect(wrapper.emitted('add-to-cart')).toHaveLength(1)
    expect(wrapper.emitted('add-to-cart')[0]).toEqual([product])
  })

  it('ปิดปุ่มและไม่ส่ง Event เมื่อสินค้าหมด', async () => {
    const wrapper = mountCard({ product: { ...product, stock: 0 } })
    const button = wrapper.get('[data-test="add-to-cart"]')

    expect(button.attributes()).toHaveProperty('disabled')
    expect(button.text()).toBe('สินค้าหมด')
    await button.trigger('click')
    expect(wrapper.emitted('add-to-cart')).toBeUndefined()
  })

  it('ซ่อนหมวดหมู่เมื่อ showCategory เป็น false', () => {
    const wrapper = mountCard({ product, showCategory: false })
    expect(wrapper.text()).not.toContain('เครื่องเสียง')
  })
})