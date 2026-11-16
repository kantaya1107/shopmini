<script setup>
import { reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { getErrorMessage } from '@/api/http'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()

const form = reactive({ email: '', password: '' })
const errors = reactive({ email: '', password: '' })
const serverError = ref('')
const submitting = ref(false)

function validate() {
  errors.email = /^\S+@\S+\.\S+$/.test(form.email) ? '' : 'กรุณากรอกอีเมลให้ถูกต้อง'
  errors.password = form.password ? '' : 'กรุณากรอกรหัสผ่าน'
  return !errors.email && !errors.password
}

async function onSubmit() {
  serverError.value = ''
  if (!validate()) return
  submitting.value = true
  try {
    await auth.login(form.email, form.password)
    // กลับไปหน้าที่ผู้ใช้ตั้งใจจะเข้าก่อนถูกพามาหน้านี้
    router.replace(route.query.redirect || '/')
  } catch (err) {
    serverError.value = getErrorMessage(err)
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <div class="mx-auto max-w-sm rounded-xl border bg-white p-6 shadow-sm">
    <h1 class="text-xl font-bold">เข้าสู่ระบบ</h1>

    <p v-if="route.query.expired" class="mt-3 rounded bg-amber-50 p-2 text-sm text-amber-700">
      เซสชันหมดอายุ กรุณาเข้าสู่ระบบอีกครั้ง
    </p>
    <p v-if="serverError" class="mt-3 rounded bg-red-50 p-2 text-sm text-red-700" data-test="server-error">
      {{ serverError }}
    </p>

    <form class="mt-4 flex flex-col gap-4" novalidate @submit.prevent="onSubmit">
      <label class="flex flex-col gap-1 text-sm">
        อีเมล
        <input v-model.trim="form.email" type="email" autocomplete="email" class="rounded-lg border px-3 py-2" :class="{ 'border-red-500': errors.email }" />
        <span v-if="errors.email" class="text-red-600">{{ errors.email }}</span>
      </label>
      <label class="flex flex-col gap-1 text-sm">
        รหัสผ่าน
        <input v-model="form.password" type="password" autocomplete="current-password" class="rounded-lg border px-3 py-2" :class="{ 'border-red-500': errors.password }" />
        <span v-if="errors.password" class="text-red-600">{{ errors.password }}</span>
      </label>
      <button class="rounded-lg bg-brand-600 py-2.5 text-white hover:bg-brand-700 disabled:opacity-60" :disabled="submitting">
        {{ submitting ? 'กำลังเข้าสู่ระบบ...' : 'เข้าสู่ระบบ' }}
      </button>
    </form>

    <p class="mt-4 text-center text-sm">
      ยังไม่มีบัญชี?
      <RouterLink :to="{ name: 'register', query: route.query }" class="text-brand-700 underline">สมัครสมาชิก</RouterLink>
    </p>
  </div>
</template>