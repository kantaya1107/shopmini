<script setup>
import { reactive, ref, onMounted } from 'vue'
import { productApi } from '@/api/products'
import { getErrorMessage } from '@/api/http'
import { formatPrice } from '@/utils/format'

const products = ref([])
const categories = ref([])
const message = ref('')
const error = ref('')

const emptyForm = () => ({ name: '', price: null, stock: 0, category_id: '', image_url: '', description: '' })
const form = reactive(emptyForm())

async function load() {
  const [page, cats] = await Promise.all([
    productApi.list({ sort: 'newest', size: 100 }),
    productApi.categories(),
  ])
  products.value = page.items
  categories.value = cats
}

async function run(action, successText) {
  error.value = ''
  message.value = ''
  try {
    await action()
    message.value = successText
    await load()
  } catch (err) {
    error.value = getErrorMessage(err)
  }
}

function createProduct() {
  return run(async () => {
    await productApi.create({ ...form, image_url: form.image_url || null })
    Object.assign(form, emptyForm())
  }, 'เพิ่มสินค้าเรียบร้อย')
}

function updateStock(product) {
  return run(() => productApi.update(product.id, { stock: product.stock }), `อัปเดตสต็อก "${product.name}" แล้ว`)
}

function removeProduct(product) {
  if (!window.confirm(`ยืนยันการลบ "${product.name}"?`)) return
  return run(() => productApi.remove(product.id), `ลบ "${product.name}" แล้ว`)
}

onMounted(load)
</script>

<template>
  <h1 class="text-2xl font-bold">จัดการสินค้า</h1>

  <p v-if="message" class="mt-3 rounded bg-green-50 p-2 text-sm text-green-700">{{ message }}</p>
  <p v-if="error" class="mt-3 rounded bg-red-50 p-2 text-sm text-red-700">{{ error }}</p>

  <form class="mt-4 grid gap-3 rounded-xl border bg-white p-4 md:grid-cols-3" @submit.prevent="createProduct">
    <input v-model.trim="form.name" required placeholder="ชื่อสินค้า" class="rounded border px-3 py-2 md:col-span-2" />
    <select v-model.number="form.category_id" required class="rounded border px-3 py-2">
      <option value="" disabled>เลือกหมวดหมู่</option>
      <option v-for="c in categories" :key="c.id" :value="c.id">{{ c.name }}</option>
    </select>
    <input v-model.number="form.price" required type="number" min="1" step="0.01" placeholder="ราคา" class="rounded border px-3 py-2" />
    <input v-model.number="form.stock" type="number" min="0" placeholder="สต็อก" class="rounded border px-3 py-2" />
    <input v-model.trim="form.image_url" placeholder="URL รูปภาพ (ไม่บังคับ)" class="rounded border px-3 py-2" />
    <button class="rounded-lg bg-brand-600 py-2 text-white md:col-span-3">เพิ่มสินค้า</button>
  </form>

  <div class="mt-6 overflow-x-auto rounded-xl border bg-white">
    <table class="w-full text-left text-sm">
      <thead class="bg-slate-50">
        <tr>
          <th class="p-3">#</th><th class="p-3">ชื่อสินค้า</th><th class="p-3">หมวดหมู่</th>
          <th class="p-3 text-right">ราคา</th><th class="p-3">สต็อก</th><th class="p-3"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in products" :key="p.id" class="border-t">
          <td class="p-3">{{ p.id }}</td>
          <td class="p-3">{{ p.name }}</td>
          <td class="p-3">{{ p.category.name }}</td>
          <td class="p-3 text-right">{{ formatPrice(p.price) }}</td>
          <td class="p-3">
            <input v-model.number="p.stock" type="number" min="0" class="w-20 rounded border px-2 py-1" />
            <button class="ml-2 text-brand-700 hover:underline" @click="updateStock(p)">บันทึก</button>
          </td>
          <td class="p-3 text-right">
            <button class="text-red-600 hover:underline" @click="removeProduct(p)">ลบ</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>ำ