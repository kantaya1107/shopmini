import { defineStore } from "pinia";
import { ref, computed, watch } from "vue";

export const useCartStore = defineStore("cart", () => {
  //State : รายการสินค้าในตะกร้า
  const items = ref([
    {
      id: 1,
      name: "Shirt",
      price: 200,
      quantiy: 1,
    },
    {
      id: 2,
      name: "Shoe",
      price: 300,
      quantiy: 3,
    }
  ]);

  //Getter : คำนวณยอดรวม
  const totalCount = computed(() => {
    return items.value.reduce((sum, item) => sum + item.quantiy, 0);
  });
  const totalPrice = computed(() => {
    return items.value.reduce(
      (sum, item) => sum + item.price * item.quantiy,
      0,
    );
  });

  //Acion
  function addToCart(product) {
    const existing = items.value.find((item) => item.id === products.id);
    if (existing) {
      existing.quantiy++;
    } else {
      items.value.push({ ...product, quantiy: 1 });
    }
  }
  return { items, totalCount, totalPrice, addToCart };
});

// const STORAGE_KEY = 'shopmini-cart'

// function loadCart() {
//   try {
//     return JSON.parse(localStorage.getItem(STORAGE_KEY)) ?? []
//   } catch {
//     return []
//   }
// }

// // Setup Store: ref = State, computed = Getters, function = Actions
// export const useCartStore = defineStore('cart', () => {
//   // ---------- State ----------
//   const items = ref(loadCart()) // [{ id, name, price, image_url, stock, qty }]

//   // ---------- Getters ----------
//   const totalItems = computed(() => items.value.reduce((sum, item) => sum + item.qty, 0))
//   const totalPrice = computed(() =>
//     items.value.reduce((sum, item) => sum + Number(item.price) * item.qty, 0),
//   )
//   const isEmpty = computed(() => items.value.length === 0)

//   // ---------- Actions ----------
//   function addItem(product, qty = 1) {
//     if (product.stock <= 0) return
//     const existing = items.value.find((item) => item.id === product.id)
//     if (existing) {
//       existing.qty = Math.min(existing.qty + qty, product.stock)
//     } else {
//       const { id, name, price, image_url, stock } = product
//       items.value.push({ id, name, price, image_url, stock, qty: Math.min(qty, stock) })
//     }
//   }

//   function increase(id) {
//     const item = items.value.find((i) => i.id === id)
//     if (item && item.qty < item.stock) item.qty++
//   }

//   function decrease(id) {
//     const item = items.value.find((i) => i.id === id)
//     if (!item) return
//     if (item.qty > 1) item.qty--
//     else removeItem(id)
//   }

//   function removeItem(id) {
//     items.value = items.value.filter((i) => i.id !== id)
//   }

//   function clear() {
//     items.value = []
//   }

//   // เก็บสถานะลง localStorage ทุกครั้งที่ตะกร้าเปลี่ยน (deep: ตรวจจับการเปลี่ยน qty ภายใน Object ด้วย)
//   watch(items, (value) => localStorage.setItem(STORAGE_KEY, JSON.stringify(value)), { deep: true })

//   return { items, totalItems, totalPrice, isEmpty, addItem, increase, decrease, removeItem, clear }
// })
