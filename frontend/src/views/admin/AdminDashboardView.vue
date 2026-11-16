<script setup>
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()
</script>

<template>
  <h1 class="text-2xl font-bold">ภาพรวมร้านค้า</h1>
  <p class="mt-2 text-slate-600">ยินดีต้อนรับ {{ auth.user?.full_name }} (สิทธิ์: {{ auth.user?.role }})</p>
  <RouterLink :to="{ name: 'admin-products' }" class="mt-4 inline-block rounded-lg bg-brand-600 px-4 py-2 text-white">
    ไปที่หน้าจัดการสินค้า
  </RouterLink>
</template>