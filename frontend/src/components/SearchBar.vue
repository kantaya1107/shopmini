<script setup>
// defineModel (Vue 3.4+) = props "modelValue" + emit "update:modelValue" ในบรรทัดเดียว
const keyword = defineModel({ type: String, default: '' })

defineProps({
  placeholder: { type: String, default: 'ค้นหาสินค้า...' },
})
</script>

<template>
  <div class="relative">
    <input
      v-model="keyword"
      type="search"
      :placeholder="placeholder"
      class="w-full rounded-lg border border-slate-300 px-4 py-2.5 focus:border-brand-600 focus:ring-2 focus:ring-brand-100 focus:outline-none"
    />
  </div>
</template>