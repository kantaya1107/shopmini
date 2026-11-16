<script setup>
defineProps({
  products: { type: Array, required: true },
})
</script>

<template>
  <section class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
    <!-- Scoped Slot: ส่งข้อมูล product แต่ละตัวออกไปให้ผู้ใช้ Component ตัดสินใจเองว่าจะแสดงอย่างไร -->
    <template v-for="product in products" :key="product.id">
      <slot :product="product" />
    </template>
  </section>
</template>