import { ref, watch, onMounted } from 'vue'
import { productApi } from '@/api/products'
import { getErrorMessage } from '@/api/http'
import { useDebounce } from './useDebounce'

export function useProducts({ size = 8 } = {}) {
  // ---------- ตัวกรอง ----------
  const keyword = ref('')
  const category = ref('all')
  const sort = ref('newest')
  const page = ref(1)
  const debouncedKeyword = useDebounce(keyword, 400)

  // ---------- ผลลัพธ์และสถานะ ----------
  const products = ref([])
  const categories = ref([])
  const total = ref(0)
  const pages = ref(0)
  const loading = ref(false)
  const error = ref('')

  async function fetchProducts() {
    loading.value = true
    error.value = ''
    try {
      const data = await productApi.list({
        search: debouncedKeyword.value || undefined,
        category: category.value === 'all' ? undefined : category.value,
        sort: sort.value,
        page: page.value,
        size,
      })
      products.value = data.items
      total.value = data.total
      pages.value = data.pages
    } catch (err) {
      error.value = getErrorMessage(err)
    } finally {
      loading.value = false
    }
  }

  async function fetchCategories() {
    try {
      categories.value = await productApi.categories()
    } catch {
      categories.value = []
    }
  }

  // เปลี่ยนตัวกรองเมื่อใด กลับไปหน้า 1 (ถ้าอยู่หน้า 1 อยู่แล้วให้โหลดใหม่ทันที)
  watch([debouncedKeyword, category, sort], () => {
    if (page.value !== 1) page.value = 1
    else fetchProducts()
  })
  watch(page, fetchProducts)

  onMounted(() => {
    fetchCategories()
    fetchProducts()
  })

  function resetFilter() {
    keyword.value = ''
    category.value = 'all'
    sort.value = 'newest'
  }

  return {
    keyword, category, sort, page,
    products, categories, total, pages, loading, error,
    fetchProducts, resetFilter,
  }
}