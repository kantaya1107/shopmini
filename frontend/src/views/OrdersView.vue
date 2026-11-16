<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { orderApi } from '@/api/orders'
import { getErrorMessage } from '@/api/http'
import { formatDate, formatPrice } from '@/utils/format'
import EmptyState from '@/components/EmptyState.vue'

const route = useRoute()
const orders = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    orders.value = await orderApi.mine()
  } catch (err) {
    error.value = getErrorMessage(err)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <h1 class="mb-6 text-2xl font-bold">ประวัติคำสั่งซื้อ</h1>

  <p v-if="route.query.created" class="mb-4 rounded-lg bg-green-50 p-3 text-green-700">
    สั่งซื้อสำเร็จ หมายเลขคำสั่งซื้อ #{{ route.query.created }}
  </p>

  <div v-if="loading" class="h-32 animate-pulse rounded-xl bg-slate-200"></div>
  <EmptyState v-else-if="error" title="โหลดข้อมูลไม่สำเร็จ">{{ error }}</EmptyState>
  <EmptyState v-else-if="!orders.length" title="ยังไม่มีคำสั่งซื้อ">
    <template #action>
      <RouterLink to="/products" class="text-brand-700 underline">เริ่มเลือกซื้อสินค้า</RouterLink>
    </template>
  </EmptyState>

  <div v-else class="flex flex-col gap-4">
    <article v-for="order in orders" :key="order.id" class="rounded-xl border bg-white p-5" data-test="order">
      <header class="flex flex-wrap items-center justify-between gap-2 border-b pb-3">
        <p class="font-semibold">คำสั่งซื้อ #{{ order.id }}</p>
        <p class="text-sm text-slate-500">{{ formatDate(order.created_at) }}</p>
        <span class="rounded bg-amber-100 px-2 py-0.5 text-xs text-amber-800">{{ order.status }}</span>
      </header>
      <ul class="divide-y">
        <li v-for="item in order.items" :key="item.product.id" class="flex justify-between py-2 text-sm">
          <span>{{ item.product.name }} x {{ item.quantity }}</span>
          <span>{{ formatPrice(item.unit_price * item.quantity) }}</span>
        </li>
      </ul>
      <p class="mt-2 text-right font-bold text-brand-700">รวม {{ formatPrice(order.total_amount) }}</p>
    </article>
  </div>
</template>