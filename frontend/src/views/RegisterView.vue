<script setup>
import { reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { getErrorMessage } from '@/api/http'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()

const form = reactive({ full_name: '', email: '', password: '', confirm: '' })
const errors = reactive({})
const serverError = ref('')
const submitting = ref(false)

function validate() {
  errors.full_name = form.full_name.length >= 2 ? '' : 'ชื่อต้องมีอย่างน้อย 2 ตัวอักษร'
  errors.email = /^\S+@\S+\.\S+$/.test(form.email) ? '' : 'รูปแบบอีเมลไม่ถูกต้อง'
  errors.password = form.password.length >= 8 ? '' : 'รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร'
  errors.confirm = form.confirm === form.password ? '' : 'รหัสผ่านทั้งสองช่องไม่ตรงกัน'
  return Object.values(errors).every((msg) => !msg)
}

async function onSubmit() {
  serverError.value = ''
  if (!validate()) return
  submitting.value = true
  try {
    const { confirm, ...payload } = form
    await auth.register(payload)
    router.replace(route.query.redirect || '/')
  } catch (err) {
    // แสดง Error รายช่องจาก Backend (VALIDATION_ERROR) ถ้ามี
    const details = err.response?.data?.error?.details
    if (Array.isArray(details)) {
      details.forEach((d) => (errors[d.field] = d.message))
    }
    serverError.value = getErrorMessage(err)
  } finally {
    submitting.value = false
  }
}

const fields = [
  { key: 'full_name', label: 'ชื่อ-นามสกุล', type: 'text', autocomplete: 'name' },
  { key: 'email', label: 'อีเมล', type: 'email', autocomplete: 'email' },
  { key: 'password', label: 'รหัสผ่าน', type: 'password', autocomplete: 'new-password' },
  { key: 'confirm', label: 'ยืนยันรหัสผ่าน', type: 'password', autocomplete: 'new-password' },
]
</script>

<template>
  <div class="mx-auto max-w-sm rounded-xl border bg-white p-6 shadow-sm">
    <h1 class="text-xl font-bold">สมัครสมาชิก</h1>
    <p v-if="serverError" class="mt-3 rounded bg-red-50 p-2 text-sm text-red-700">{{ serverError }}</p>

    <form class="mt-4 flex flex-col gap-4" novalidate @submit.prevent="onSubmit">
      <label v-for="f in fields" :key="f.key" class="flex flex-col gap-1 text-sm">
        {{ f.label }}
        <input
          v-model.trim="form[f.key]"
          :type="f.type"
          :autocomplete="f.autocomplete"
          class="rounded-lg border px-3 py-2"
          :class="{ 'border-red-500': errors[f.key] }"
        />
        <span v-if="errors[f.key]" class="text-red-600">{{ errors[f.key] }}</span>
      </label>
      <button class="rounded-lg bg-brand-600 py-2.5 text-white hover:bg-brand-700 disabled:opacity-60" :disabled="submitting">
        {{ submitting ? 'กำลังสมัคร...' : 'สมัครสมาชิก' }}
      </button>
    </form>
  </div>
</template>