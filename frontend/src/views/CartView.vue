<!-- <script setup>
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/cart'
import { formatPrice } from '@/utils/format'
import EmptyState from '@/components/EmptyState.vue'

const cart = useCartStore()
const { items, totalItems, totalPrice, isEmpty } = storeToRefs(cart)
</script>

<template>
  <h1 class="mb-6 text-2xl font-bold">ตะกร้าสินค้า</h1>

  <EmptyState v-if="isEmpty" title="ตะกร้าว่างเปล่า">
    ยังไม่มีสินค้าในตะกร้า
    <template #action>
      <RouterLink to="/products" class="rounded-lg bg-brand-600 px-4 py-2 text-white">เลือกซื้อสินค้า</RouterLink>
    </template>
  </EmptyState>

  <div v-else class="grid gap-6 lg:grid-cols-3">
    <ul class="divide-y rounded-xl border bg-white lg:col-span-2">
      <li v-for="item in items" :key="item.id" class="flex items-center gap-4 p-4">
        <img :src="item.image_url" :alt="item.name" class="h-16 w-16 rounded-lg object-cover" />
        <div class="flex-1">
          <p class="font-semibold">{{ item.name }}</p>
          <p class="text-sm text-slate-500">{{ formatPrice(item.price) }}</p>
        </div>
        <div class="flex items-center gap-2">
          <button class="h-8 w-8 rounded border" @click="cart.decrease(item.id)">-</button>
          <span class="w-8 text-center">{{ item.qty }}</span>
          <button class="h-8 w-8 rounded border disabled:opacity-40" :disabled="item.qty >= item.stock" @click="cart.increase(item.id)">+</button>
        </div>
        <p class="w-28 text-right font-semibold">{{ formatPrice(item.price * item.qty) }}</p>
        <button class="text-sm text-red-600 hover:underline" @click="cart.removeItem(item.id)">ลบ</button>
      </li>
    </ul>

    <aside class="h-fit rounded-xl border bg-white p-6">
      <p class="flex justify-between"><span>จำนวนสินค้า</span><span>{{ totalItems }} ชิ้น</span></p>
      <p class="mt-2 flex justify-between text-lg font-bold">
        <span>ยอดรวม</span><span class="text-brand-700">{{ formatPrice(totalPrice) }}</span>
      </p>
      <button class="mt-6 w-full rounded-lg bg-brand-600 py-2.5 text-white hover:bg-brand-700">
        สั่งซื้อ (เปิดใช้วันที่ 4)
      </button>
      <button class="mt-2 w-full text-sm text-slate-500 hover:underline" @click="cart.clear()">ล้างตะกร้า</button>
    </aside>
  </div>
</template> -->

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'
import { useCartStore } from '@/stores/cart'
import { useAuthStore } from '@/stores/auth'
import { orderApi } from '@/api/orders'
import { getErrorMessage } from '@/api/http'
import { formatPrice } from '@/utils/format'
import EmptyState from '@/components/EmptyState.vue'

const router = useRouter()
const cart = useCartStore()
const auth = useAuthStore()
const { items, totalItems, totalPrice, isEmpty } = storeToRefs(cart)

const placing = ref(false)
const error = ref('')
const shortages = ref([])

async function checkout() {
  if (!auth.isAuthenticated) {
    router.push({ name: 'login', query: { redirect: '/cart' } })
    return
  }
  placing.value = true
  error.value = ''
  shortages.value = []
  try {
    const order = await orderApi.create(
      items.value.map((item) => ({ product_id: item.id, quantity: item.qty })),
    )
    cart.clear()
    router.push({ name: 'orders', query: { created: order.id } })
  } catch (err) {
    error.value = getErrorMessage(err)
    if (err.response?.data?.error?.code === 'INSUFFICIENT_STOCK') {
      shortages.value = err.response.data.error.details
    }
  } finally {
    placing.value = false
  }
}
</script>

<template>
  <h1 class="mb-6 text-2xl font-bold">ตะกร้าสินค้า</h1>

  <EmptyState v-if="isEmpty" title="ตะกร้าว่างเปล่า">
    ยังไม่มีสินค้าในตะกร้า
    <template #action>
      <RouterLink to="/products" class="rounded-lg bg-brand-600 px-4 py-2 text-white">เลือกซื้อสินค้า</RouterLink>
    </template>
  </EmptyState>

  <div v-else class="grid gap-6 lg:grid-cols-3">
    <ul class="divide-y rounded-xl border bg-white lg:col-span-2">
      <li v-for="item in items" :key="item.id" class="flex items-center gap-4 p-4">
        <img :src="item.image_url" :alt="item.name" class="h-16 w-16 rounded-lg object-cover" />
        <div class="flex-1">
          <p class="font-semibold">{{ item.name }}</p>
          <p class="text-sm text-slate-500">{{ formatPrice(item.price) }}</p>
        </div>
        <div class="flex items-center gap-2">
          <button class="h-8 w-8 rounded border" @click="cart.decrease(item.id)">-</button>
          <span class="w-8 text-center">{{ item.qty }}</span>
          <button class="h-8 w-8 rounded border disabled:opacity-40" :disabled="item.qty >= item.stock" @click="cart.increase(item.id)">+</button>
        </div>
        <p class="w-28 text-right font-semibold">{{ formatPrice(item.price * item.qty) }}</p>
        <button class="text-sm text-red-600 hover:underline" @click="cart.removeItem(item.id)">ลบ</button>
      </li>
    </ul>

    <aside class="h-fit rounded-xl border bg-white p-6">
      <p class="flex justify-between"><span>จำนวนสินค้า</span><span>{{ totalItems }} ชิ้น</span></p>
      <p class="mt-2 flex justify-between text-lg font-bold">
        <span>ยอดรวม</span><span class="text-brand-700">{{ formatPrice(totalPrice) }}</span>
      </p>

      <div v-if="error" class="mt-4 rounded bg-red-50 p-3 text-sm text-red-700" data-test="checkout-error">
        <p>{{ error }}</p>
        <ul v-if="shortages.length" class="mt-1 list-disc pl-5">
          <li v-for="s in shortages" :key="s.product_id">{{ s.name }}: เหลือ {{ s.available }} ชิ้น</li>
        </ul>
      </div>

      <button
        class="mt-6 w-full rounded-lg bg-brand-600 py-2.5 text-white hover:bg-brand-700 disabled:opacity-60"
        :disabled="placing"
        @click="checkout"
      >
        {{ placing ? 'กำลังสั่งซื้อ...' : auth.isAuthenticated ? 'ยืนยันการสั่งซื้อ' : 'เข้าสู่ระบบเพื่อสั่งซื้อ' }}
      </button>
      <button class="mt-2 w-full text-sm text-slate-500 hover:underline" @click="cart.clear()">ล้างตะกร้า</button>
    </aside>
  </div>
</template>