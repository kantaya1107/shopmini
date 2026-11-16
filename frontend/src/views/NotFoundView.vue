<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
</script>

<template>
  <div class="py-20 text-center">
    <p class="text-6xl font-bold text-brand-700">404</p>
    <p class="mt-2">ไม่พบหน้า <code class="rounded bg-slate-100 px-1">{{ route.fullPath }}</code></p>
    <RouterLink to="/" class="mt-6 inline-block text-brand-700 underline">กลับหน้าแรก</RouterLink>
  </div>
</template>