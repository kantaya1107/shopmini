// // Promise จำลองการรอข้อมูลจาก Server 1 วินาที
// const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms))

// async function demoOrder() {
//   console.log('1) ส่งคำสั่งซื้อ...')
//   await wait(1000)
//   console.log('2) ได้รับการยืนยันแล้ว')
// }

// // เรียก Public API ด้วย fetch + async/await + try/catch
// async function loadProducts() {
//   try {
//     const res = await fetch('https://dummyjson.com/products?limit=30&select=title,price,category')
//     if (!res.ok) throw new Error(`HTTP ${res.status}`)
//     const data = await res.json()

//     const groceries = data.products
//       .filter((p) => p.category === 'groceries')
//       .map((p) => `${p.title} - $${p.price}`)

//     console.log(`3) ดึงสินค้าได้ ${data.products.length} รายการ จากทั้งหมด ${data.total}`)
//     console.log('4) หมวด groceries:', groceries.slice(0, 3))
//   } catch (err) {
//     console.error('เรียก API ไม่สำเร็จ:', err.message)
//   }
// }

// await demoOrder()
// await loadProducts()

async function loadProducts() {
  try {
    const response = await fetch('https://dummyjson.com/products?limit=30&select=title,price,category');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log('data : ', data);
  } catch (err) {
    console.log("Error:", err.message);
  }
}

await loadProducts();
