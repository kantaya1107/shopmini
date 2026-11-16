<script setup>
import { ref, onMounted } from 'vue'
import { productApi } from '@/api/products'
import ProductCard from '@/components/ProductCard.vue'
import ProductSkeleton from '@/components/ProductSkeleton.vue'
import { useCartStore } from '@/stores/cart'

const cart = useCartStore()
const featured = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const data = await productApi.list({ sort: 'newest', size: 8 })
    featured.value = data.items
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="mb-8 rounded-2xl bg-brand-700 p-8 text-white md:p-12">
    <h1 class="text-3xl font-bold md:text-4xl">ShopMini</h1>
    <p class="mt-2 text-brand-100">อุปกรณ์ไอทีคุณภาพ ส่งไวทั่วประเทศ</p>
    <RouterLink to="/products" class="mt-6 inline-block rounded-lg bg-white px-5 py-2 font-semibold text-brand-700">
      เลือกซื้อสินค้า
    </RouterLink>
  </section>

  <h2 class="mb-4 text-xl font-semibold">สินค้าใหม่ล่าสุด</h2>
  <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
    <template v-if="loading">
      <ProductSkeleton v-for="n in 4" :key="n" />
    </template>
    <template v-else>
      <ProductCard v-for="p in featured" :key="p.id" :product="p" @add-to-cart="cart.addItem" />
    </template>
  </div>
</template>