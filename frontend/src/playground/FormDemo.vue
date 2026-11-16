<script setup>
import { reactive , computed} from 'vue'
const form = reactive({
    name: '',
    email: '',
    quantity: '',
    shipping: 'standard',
    acceptTerms: false
})
const canSubmit = computed(()=> form.name.trim() && form.email.includes('@') && form.quantity > 0 && form.acceptTerms)
const submitForm = () => {
    alert(`สั่งซื้อ ${form.quantity} ชิ้น ส่งแบบ ${form.shipping}`)
}
</script>

<template>
    <div>
        <h2>Form Demo</h2>
        <form @submit.prevent="submitForm">
            <div class="input">
                <input v-model.trim="form.name" type="text" placeholder="ชื่อผู้สั่งซื้อ" />
            </div>
            <div class="input">
                <input v-model.trim="form.email" type="email" placeholder="อีเมล" />
            </div>
            <div class="input">
                <input v-model.number="form.quantity" type="number" placeholder="จำนวน" />
            </div>
            <div class="input">
                <select v-model="form.shipping" name="shipping" id="shipping">
                    <option value="standard">ส่งธรรมดา</option>
                    <option value="express">ส่งด่วน</option>
                </select>
            </div>
            <div class="input">
                <label>
                    <input v-model="form.acceptTerms" type="checkbox" />
                    ยอมรับเงื่อนไข
                </label>
            </div>
            <div class="input">
                <button :disabled="!canSubmit">ยืนยัน</button>
            </div>
            <pre>{{ form }}</pre>
        </form>
    </div>
</template>

<style lang="css" scoped>
.input {
    margin: 10px;
}
</style>