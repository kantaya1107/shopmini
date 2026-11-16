<script setup>
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { productApi } from '@/api/products'
import { getErrorMessage } from '@/api/http'
import { useCartStore } from '@/stores/cart'
import { formatPrice } from '@/utils/format'
import EmptyState from '@/components/EmptyState.vue'

const route = useRoute()
const router = useRouter()
const cart = useCartStore()

const product = ref(null)
const loading = ref(true)
const error = ref('')
const qty = ref(1)

async function loadProduct(id) {
  loading.value = true
  error.value = ''
  product.value = null
  try {
    product.value = await productApi.get(id)
    qty.value = 1
  } catch (err) {
    error.value = err.response?.status === 404 ? '' : getErrorMessage(err)
  } finally {
    loading.value = false
  }
}

// โหลดใหม่ทุกครั้งที่ id ใน URL เปลี่ยน (Component เดิมถูกใช้ซ้ำ ไม่ถูกสร้างใหม่)
watch(() => route.params.id, loadProduct, { immediate: true })

function addAndGoToCart() {
  cart.addItem(product.value, qty.value)
  router.push({ name: 'cart' })
}
</script>

<template>
  <button class="mb-4 text-sm text-brand-700 hover:underline" @click="router.back()">← ย้อนกลับ</button>

  <div v-if="loading" class="grid animate-pulse gap-8 md:grid-cols-2">
    <div class="aspect-4/3 rounded-2xl bg-slate-200"></div>
    <div class="flex flex-col gap-4">
      <div class="h-8 w-2/3 rounded bg-slate-200"></div>
      <div class="h-4 w-full rounded bg-slate-200"></div>
      <div class="h-8 w-1/3 rounded bg-slate-200"></div>
    </div>
  </div>

  <EmptyState v-else-if="error" title="โหลดข้อมูลไม่สำเร็จ">{{ error }}</EmptyState>

  <div v-else-if="product" class="grid gap-8 md:grid-cols-2">
    <img :src="product.image_url" :alt="product.name" class="w-full rounded-2xl object-cover" />
    <div class="flex flex-col gap-4">
      <span class="w-fit rounded bg-brand-50 px-2 py-0.5 text-sm text-brand-700">{{ product.category.name }}</span>
      <h1 class="text-3xl font-bold">{{ product.name }}</h1>
      <p class="text-slate-600">{{ product.description }}</p>
      <p class="text-2xl font-bold text-brand-700">{{ formatPrice(product.price) }}</p>
      <p class="text-sm" :class="product.stock > 0 ? 'text-slate-500' : 'text-red-600'">
        {{ product.stock > 0 ? `คงเหลือ ${product.stock} ชิ้น` : 'สินค้าหมด' }}
      </p>
      <div v-if="product.stock > 0" class="flex items-center gap-3">
        <input v-model.number="qty" type="number" min="1" :max="product.stock" class="w-20 rounded-lg border px-3 py-2" />
        <button class="rounded-lg bg-brand-600 px-6 py-2 text-white hover:bg-brand-700" @click="addAndGoToCart">
          ใส่ตะกร้าและไปที่ตะกร้า
        </button>
      </div>
    </div>
  </div>

  <EmptyState v-else title="ไม่พบสินค้านี้">
    สินค้ารหัส {{ route.params.id }} อาจถูกลบไปแล้ว
    <template #action>
      <RouterLink to="/products" class="text-brand-700 underline">กลับไปหน้ารายการสินค้า</RouterLink>
    </template>
  </EmptyState>
</template>