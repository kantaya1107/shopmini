<script setup>
import { ref } from 'vue'
// import { products } from '@/data/products'
import ProductCard from '@/components/ProductCard.vue'
import SearchBar from '@/components/SearchBar.vue'
import CategoryFilter from '@/components/CategoryFilter.vue'
import EmptyState from '@/components/EmptyState.vue'
import LifecycleDemo from '@/playground/LifecycleDemo.vue'
import ProductGrid from '@/components/ProductGrid.vue'
import { useProducts } from '@/composables/useProducts'

const { keyword, category, categories, products, total, resetFilter } = useProducts()
const showDemo = ref(true)

function onAddToCart(product) {
    console.log('เพิ่มลงตะกร้า:', product.name)
}
</script>

<template>
    <main class="mx-auto max-w-6xl p-3 space-y-1 ">
        <div class="flex justify-center text-2xl text-brand-700 mb-3">App Test</div>
        <button class="mb-2 text-sm underline" @click="showDemo = !showDemo">แสดง/ซ่อน LifecycleDemo</button>
        <LifecycleDemo v-if="showDemo" class="mb-6" />
        <SearchBar placeholder="ค้นหาสินค้า" v-model="keyword" />
        <p class="my-2 text-sm">Keyword : {{ keyword }}</p>
        <CategoryFilter :categories="categories" :selected="category" @change="category = $event" />
        <div class="grid">
            <!-- <div class="grid md:grid-cols-4 grid-cols-2 gap-3 p-2">
                <div v-for="product in products">
                    <ProductCard :product="product" @add-to-cart="onAddToCart" />
                </div>
            </div> -->
            <ProductGrid v-if="products.length" :products="products">
                <template #default="{ product }">
                    <ProductCard :product="product" @add-to-cart="onAddToCart" />
                </template>
            </ProductGrid>
            <EmptyState :title="'ไม่พบสินค้า'">
                <p>ลองเปลี่ยนคำค้นหา</p>
                <template #action>
                    <button class=" rounded-2xl p-2 border-2 hover:bg-red-50" @click="">
                        ล้างตัวกรอง
                    </button>
                </template>
            </EmptyState>
        </div>


    </main>
</template>


<style lang="scss" scoped></style>