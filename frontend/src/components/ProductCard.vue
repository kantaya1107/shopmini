<script setup>
import { computed } from 'vue'
import { formatPrice } from '@/utils/format'

const props = defineProps({
  product: { type: Object, required: true },
  showCategory: { type: Boolean, default: true },
})

const emit = defineEmits(['add-to-cart'])

const isOutOfStock = computed(() => props.product.stock <= 0)
</script>

<template>
  <article class="flex flex-col overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm transition hover:shadow-md">
    <RouterLink :to="{ name: 'product-detail', params: { id: product.id } }">
      <img :src="product.image_url" :alt="product.name" class="aspect-4/3 w-full object-cover" loading="lazy" />
    </RouterLink>

    <div class="flex flex-1 flex-col gap-2 p-4">
      <span v-if="showCategory" class="w-fit rounded bg-brand-50 px-2 py-0.5 text-xs text-brand-700">
        {{ product.category?.name }}
      </span>
      <RouterLink
        :to="{ name: 'product-detail', params: { id: product.id } }"
        class="font-semibold hover:text-brand-700"
        data-test="product-name"
      >
        {{ product.name }}
      </RouterLink>
      <p class="text-lg font-bold text-brand-700" data-test="product-price">{{ formatPrice(product.price) }}</p>

      <button
        class="mt-auto rounded-lg bg-brand-600 px-4 py-2 text-white hover:bg-brand-700 disabled:cursor-not-allowed disabled:bg-slate-300"
        :disabled="isOutOfStock"
        data-test="add-to-cart"
        @click="emit('add-to-cart', product)"
      >
        {{ isOutOfStock ? 'สินค้าหมด' : 'ใส่ตะกร้า' }}
      </button>
    </div>
  </article>
</template>