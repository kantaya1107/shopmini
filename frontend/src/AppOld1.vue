<script setup>
import { ref, reactive, computed } from "vue";

const name = "Kan";
const count = ref(0); //ใช้ ref สำหรับสร้าง state ที่เป็น primitive type เช่น string, number, boolean
const cart = reactive({ //ใช้ reactive สำหรับสร้าง state ที่เป็น object หรือ array
  items: 5,
  price: 590
});
// computed ใช้สำหรับสร้างค่าที่คำนวณจาก state อื่น ๆ และจะถูกคำนวณใหม่เมื่อ state ที่เกี่ยวข้องเปลี่ยนแปลง
const total = computed(() => {
  return cart.items * cart.price;
});

function addItem() {
  cart.items++;
};
function deleteItem() {
  cart.items--;
};
</script>

<template>
  <h1>Hello, {{ name }}</h1>
  <button @click="count++">+</button>
  <h1>Click Count: {{ count }}</h1>
  <button @click="count--">-</button>
  <h1>Cart: {{ cart.items }} items,${{ cart.price }}</h1>
  <h1>Total: ${{ total }}</h1>
  <div>
    <button @click="addItem">Add Item</button>
    <button @click="deleteItem">Delete Item</button>
  </div>

</template>

<style scoped>
body {
  background-color: #93e1f5;
}

h1 {
  color: red;
}
</style>