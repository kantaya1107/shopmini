import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { effectScope, ref, nextTick } from 'vue'
import { useDebounce } from '../useDebounce'

describe('useDebounce', () => {
  beforeEach(() => vi.useFakeTimers())
  afterEach(() => vi.useRealTimers())

  it('อัปเดตค่าหลังผู้ใช้หยุดพิมพ์ครบเวลาที่กำหนดเท่านั้น', async () => {
    // effectScope จำลองบริบทของ Component ให้ watch และ onScopeDispose ทำงานได้
    const scope = effectScope()
    const keyword = ref('')
    const debounced = scope.run(() => useDebounce(keyword, 300))

    keyword.value = 'ห'
    await nextTick()
    keyword.value = 'หูฟัง'
    await nextTick()

    vi.advanceTimersByTime(299)
    expect(debounced.value).toBe('')

    vi.advanceTimersByTime(1)
    expect(debounced.value).toBe('หูฟัง')

    scope.stop()
  })
})