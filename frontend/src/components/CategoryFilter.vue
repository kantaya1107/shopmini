<script setup>
// ตัวอย่างการสื่อสารแบบ Props ลง + Emits ขึ้น (One-way Data Flow) แบบเขียนเต็ม
defineProps({
  categories: { type: Array, required: true },
  selected: { type: String, default: 'all' },
})

const emit = defineEmits(['change'])
</script>

<template>
  <nav class="flex flex-wrap gap-2">
    <button
      v-for="c in [{ slug: 'all', name: 'ทั้งหมด' }, ...categories]"
      :key="c.slug"
      class="rounded-full border px-4 py-1.5 text-sm transition"
      :class="selected === c.slug
        ? 'border-brand-700 bg-brand-700 text-white'
        : 'border-slate-300 bg-white hover:border-brand-600'"
      @click="emit('change', c.slug)"
    >
      {{ c.name }}
    </button>
  </nav>
</template>