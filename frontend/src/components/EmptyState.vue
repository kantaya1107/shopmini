<script setup>
defineProps({
  title: { type: String, default: 'ไม่พบข้อมูล' },
})
</script>

<template>
  <div class="rounded-xl border border-dashed border-slate-300 bg-white p-10 text-center">
    <p class="text-lg font-semibold">{{ title }}</p>
    <!-- Default Slot: ข้อความอธิบาย -->
    <div class="mt-1 text-slate-500"><slot /></div>
    <!-- Named Slot: ปุ่มการกระทำ (แสดงเฉพาะเมื่อผู้ใช้ส่งมา) -->
    <div v-if="$slots.action" class="mt-4"><slot name="action" /></div>
  </div>
</template>