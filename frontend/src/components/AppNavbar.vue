<script setup>
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const { totalItems } = storeToRefs(useCartStore())
const auth = useAuthStore()

function logout() {
  auth.logout()
  router.push({ name: 'home' })
}
</script>

<template>
  <header class="sticky top-0 z-10 border-b border-slate-200 bg-white/90 backdrop-blur">
    <nav class="mx-auto flex max-w-6xl items-center gap-6 px-4 py-3">
      <RouterLink to="/" class="text-xl font-bold text-brand-700">ShopMini</RouterLink>

      <div class="flex flex-1 gap-4 text-sm">
        <RouterLink to="/products" class="hover:text-brand-700" active-class="font-semibold text-brand-700">สินค้า</RouterLink>
        <RouterLink v-if="auth.isAuthenticated" to="/orders" class="hover:text-brand-700" active-class="font-semibold text-brand-700">
          คำสั่งซื้อของฉัน
        </RouterLink>
        <!-- แสดงเมนูผู้ดูแลระบบเฉพาะผู้ที่มี role = admin -->
        <RouterLink v-if="auth.isAdmin" to="/admin" class="hover:text-brand-700" active-class="font-semibold text-brand-700">
          ผู้ดูแลระบบ
        </RouterLink>
      </div>

      <RouterLink to="/cart" class="relative rounded-lg px-3 py-1.5 hover:bg-slate-100">
        ตะกร้า
        <span v-if="totalItems > 0" class="absolute -top-1 -right-2 rounded-full bg-red-500 px-1.5 text-xs text-white" data-test="cart-badge">
          {{ totalItems }}
        </span>
      </RouterLink>

      <template v-if="auth.isAuthenticated">
        <span class="hidden text-sm text-slate-600 sm:inline" data-test="user-name">{{ auth.user?.full_name }}</span>
        <button class="rounded-lg border px-3 py-1.5 text-sm hover:bg-slate-100" @click="logout">ออกจากระบบ</button>
      </template>
      <RouterLink v-else to="/login" class="rounded-lg bg-brand-600 px-3 py-1.5 text-sm text-white hover:bg-brand-700">
        เข้าสู่ระบบ
      </RouterLink>
    </nav>
  </header>
</template>