<script setup>
import { ref, watch, watchEffect, onMounted, onUpdated, onUnmounted } from 'vue'
const width = ref(window.innerWidth)
const keyword = ref('')
const category = ref('all')
const logs = ref([])

function onResize() {
    width.value = window.innerWidth
}
//ครั้งแรก ที่โหลดหน้าจอ คล้าย useEffect
onMounted(() => {
    // เหมาะกับงานที่ต้องใช้ DOM จริง หรือผูก Event กับ window
    window.addEventListener('resize', onResize)
    logs.value.push('onMounted: Component ถูกวางบนหน้าจอแล้ว')
})

//ไม่จำเป็นอย่าใช้ เปลืองแรม
onUpdated(() => {
    // ห้ามแก้ State ในนี้ (จะวนอัปเดตไม่รู้จบ) ใช้สำหรับอ่าน DOM หลังอัปเดตเท่านั้น
    console.log('onUpdated: DOM อัปเดตแล้ว')
})

onUnmounted(() => {
    // คืนทรัพยากรเสมอ ไม่เช่นนั้น Listener จะค้างอยู่แม้ Component ถูกทำลายแล้ว (Memory Leak)
    window.removeEventListener('resize', onResize)
    console.log('onUnmounted: ถอด Event Listener แล้ว')
})

// watch: ระบุสิ่งที่ต้องการเฝ้าชัดเจน ได้ค่าใหม่และค่าเก่า ไม่ทำงานตอนเริ่มต้น (เว้นแต่ใส่ immediate: true)
watch(keyword, (newValue, oldValue) => {
    logs.value.push(`watch: "${oldValue}" -> "${newValue}"`)
})

// watchEffect: ทำงานทันที 1 ครั้ง แล้วติดตามทุก ref ที่ถูกอ่านภายในโดยอัตโนมัติ
watchEffect(() => {
    console.log(`watchEffect: ค้นหา "${keyword.value}" ในหมวด ${category.value}`)
})

</script>

<template>
  <section class="rounded-xl border bg-white p-4">
    <p>ความกว้างหน้าต่าง: {{ width }}px</p>
    <input v-model="keyword" class="mt-2 rounded border px-3 py-1" placeholder="พิมพ์เพื่อดู watch" />
    <select v-model="category" class="ml-2 rounded border px-3 py-1">
      <option value="all">ทั้งหมด</option>
      <option value="audio">เครื่องเสียง</option>
    </select>
    <ul class="mt-3 list-disc pl-5 text-sm">
      <li v-for="(log, i) in logs" :key="i">{{ log }}</li>
    </ul>
  </section>
</template>

<style scoped></style>