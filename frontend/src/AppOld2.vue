<script setup>
import { ref, computed } from 'vue'
import { products, categories } from './data/products.js'
const formatPrice = (value) => {
    return new Intl.NumberFormat('th-TH', { style: 'currency', currency: 'THB' }).format(value);
}
const keyword = ref('');
const selectedCategory = ref('all');

//function สำหรับค้นหา
const filteredProducts = computed(() => {
    const q = keyword.value.trim().toLowerCase()
    return products.filter((p) => {
        const matchKeyword = p.name.toLowerCase().includes(q)
        const matchCategory = selectedCategory.value === 'all' || p.category.slug === selectedCategory.value
        return matchKeyword && matchCategory
    })
})

// function ล้างข้อมูลที่ค้นหา
function resetFilter() {
    keyword.value = ''
    selectedCategory.value = 'all'
}
</script>

<template>
    <main class="container">

        <header class="page-header">
            <div class="flex justify-center md:text-[40px]">
                <h1>Shop Mini</h1>
            </div>
            <div class="mb-3 p-2 rounded-2xl bg-brand-100">
                <input v-model="keyword" class="search" type="search" placeholder="ค้นหาชื่อสินค้า..." />
                <p :class="filteredProducts.length<=0?'text-red-500':'text-amber-950'">พบสินค้า {{ filteredProducts.length }} จาก {{ products.length }} รายการ</p>
            </div>
        </header>
        <nav class="filters">
            <button :class="{ active: selectedCategory === 'all' }" @click="selectedCategory = 'all'">
                ทั้งหมด
            </button>
            <button v-for="c in categories" :key="c.slug" :class="{ active: selectedCategory === c.slug }"
                @click="selectedCategory = c.slug">
                {{ c.name }}
            </button>
        </nav>
        <section v-if="filteredProducts.length" class="grid">
            <article v-for="p in filteredProducts" :key="p.id" class="card">
                <img :src="p.image_url" :alt="p.name" loading="lazy" />
                <span class="badge">{{ p.category.name }}</span>
                <h3>{{ p.name }}</h3>
                <p class="price">{{ formatPrice(p.price) }}</p>
                <p v-if="p.stock === 0" class="out">สินค้าหมด</p>
                <p v-else class="stock">คงเหลือ {{ p.stock }} ชิ้น</p>
            </article>
        </section>

        <section v-else class="empty">
            <p>ไม่พบสินค้าที่ตรงกับ "{{ keyword }}"</p>
            <button @click="resetFilter">ล้างตัวกรอง</button>
        </section>
        <!-- <section class="grid">
            <article class="card" v-for="p in filteredProducts" :key="p.id">
                <img :src="p.image_url" :alt="p.name" />
                <span class="badge">{{ p.category.name }}</span>
                <h3>{{ p.name }}</h3>
                <p class="price">{{ formatPrice(p.price) }}</p>
                <p class="stock">{{ p.stock }} in stock</p>
            </article>
        </section> -->
    </main>
</template>

<style scoped>
.container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 24px;
}

.page-header h1 {
    margin: 0;
    color: #0f766e;
}

.search {
    width: 100%;
    padding: 10px 14px;
    margin: 16px 0;
    font-size: 16px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
}

.filters {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 20px;
}

.filters button {
    padding: 6px 14px;
    border: 1px solid #0f766e;
    background: #fff;
    color: #0f766e;
    border-radius: 999px;
    cursor: pointer;
}

.filters button.active {
    background: #0f766e;
    color: #fff;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 16px;
}

.card {
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 12px;
}

.card img {
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    border-radius: 8px;
}

.badge {
    font-size: 12px;
    background: #f1f5f9;
    padding: 2px 8px;
    border-radius: 6px;
}

.price {
    font-weight: 700;
    color: #0f766e;
}

.out {
    color: #dc2626;
}

.stock {
    color: #64748b;
    font-size: 14px;
}

.empty {
    text-align: center;
    padding: 48px;
    color: #64748b;
}
</style>