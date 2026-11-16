<script setup>
import { ref } from 'vue'

const isLoggedIn = ref(false)
const showDetail = ref(true)
const imageUrl = ref('https://picsum.photos/seed/shopmini-5/200/150')
const tags = ref(['ใหม่', 'ขายดี', 'ส่งฟรี'])
</script>

<template>
    <section>
        <h2>Directive Demo</h2>
        <img :src="imageUrl" alt="Random Image" />
        <p></p>
        <button @click="isLoggedIn = !isLoggedIn">
            {{ isLoggedIn ? 'ออกจากระบบ' : 'เข้าสู่ระบบ' }}
        </button>
        <p v-if="isLoggedIn">เข้าสู่ระบบแล้ว</p>
        <p v-else>ยังไม่ได้เข้าสู่ระบบ</p>
        <button @click="showDetail = !showDetail">
            {{ showDetail ? 'ซ่อนรายละเอียด' : 'แสดงรายละเอียด' }}
        </button>
        <p v-show="showDetail">รายละเอียดสินค้า</p>
        <ul>
            <li v-for="(tag,index) in tags">
                {{index + 1}} {{tag }}
            </li>
        </ul>
    </section>
</template>

<style scoped></style>
