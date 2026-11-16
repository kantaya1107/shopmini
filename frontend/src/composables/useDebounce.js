import { ref, watch, onScopeDispose } from 'vue'

// คืน ref ใหม่ที่อัปเดตตาม source หลังจากผู้ใช้หยุดพิมพ์ครบ delay มิลลิวินาที
export function useDebounce(source, delay = 300) {
  const debounced = ref(source.value)
  let timer = null

  watch(source, (value) => {
    clearTimeout(timer)
    timer = setTimeout(() => {
      debounced.value = value
    }, delay)
  })

  // ล้าง timer เมื่อ Component ที่เรียกใช้ถูกทำลาย
  onScopeDispose(() => clearTimeout(timer))

  return debounced
}