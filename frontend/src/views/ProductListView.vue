<script setup>
import SearchBar from '@/components/SearchBar.vue'
import CategoryFilter from '@/components/CategoryFilter.vue'
import ProductGrid from '@/components/ProductGrid.vue'
import ProductCard from '@/components/ProductCard.vue'
import ProductSkeleton from '@/components/ProductSkeleton.vue'
import EmptyState from '@/components/EmptyState.vue'
import { useProducts } from '@/composables/useProducts'
import { useCartStore } from '@/stores/cart'

const {
  keyword, category, sort, page,
  products, categories, total, pages, loading, error,
  fetchProducts, resetFilter,
} = useProducts({ size: 8 })
const cart = useCartStore()
</script>

<template>
  <div class="mb-6 flex flex-col gap-4">
    <h1 class="text-2xl font-bold">สินค้าทั้งหมด</h1>
    <div class="flex flex-col gap-3 md:flex-row">
      <SearchBar v-model="keyword" class="flex-1" />
      <select v-model="sort" class="rounded-lg border border-slate-300 bg-white px-3 py-2.5">
        <option value="newest">ใหม่ล่าสุด</option>
        <option value="price_asc">ราคาต่ำไปสูง</option>
        <option value="price_desc">ราคาสูงไปต่ำ</option>
        <option value="name">ชื่อ ก-ฮ</option>
      </select>
    </div>
    <CategoryFilter :categories="categories" :selected="category" @change="category = $event" />
    <p v-if="!loading && !error" class="text-sm text-slate-500">พบสินค้า {{ total }} รายการ</p>
  </div>

  <!-- 1) Loading: แสดง Skeleton แทน Spinner -->
  <div v-if="loading" class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
    <ProductSkeleton v-for="n in 8" :key="n" />
  </div>

  <!-- 2) Error -->
  <EmptyState v-else-if="error" title="โหลดข้อมูลไม่สำเร็จ">
    {{ error }}
    <template #action>
      <button class="rounded-lg bg-brand-600 px-4 py-2 text-white" @click="fetchProducts">ลองใหม่</button>
    </template>
  </EmptyState>

  <!-- 3) Empty -->
  <EmptyState v-else-if="!products.length" title="ไม่พบสินค้า">
    ลองเปลี่ยนคำค้นหาหรือเลือกหมวดหมู่อื่น
    <template #action>
      <button class="rounded-lg border px-4 py-2 hover:bg-slate-100" @click="resetFilter">ล้างตัวกรอง</button>
    </template>
  </EmptyState>

  <!-- 4) Success -->
  <template v-else>
    <ProductGrid :products="products">
      <template #default="{ product }">
        <ProductCard :product="product" @add-to-cart="cart.addItem" />
      </template>
    </ProductGrid>

    <nav v-if="pages > 1" class="mt-8 flex items-center justify-center gap-4">
      <button class="rounded-lg border px-4 py-2 disabled:opacity-40" :disabled="page <= 1" @click="page--">ก่อนหน้า</button>
      <span class="text-sm">หน้า {{ page }} / {{ pages }}</span>
      <button class="rounded-lg border px-4 py-2 disabled:opacity-40" :disabled="page >= pages" @click="page++">ถัดไป</button>
    </nav>
  </template>
</template>