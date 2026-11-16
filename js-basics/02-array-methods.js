const products = [
  { id: 1, name: 'เมาส์ไร้สาย', price: 590, category: 'accessories', stock: 25 },
  { id: 2, name: 'คีย์บอร์ด Mechanical', price: 1890, category: 'accessories', stock: 12 },
  { id: 5, name: 'หูฟังบลูทูธ ANC', price: 2490, category: 'audio', stock: 10 },
  { id: 8, name: 'สายชาร์จ USB-C', price: 250, category: 'mobile', stock: 60 },
  { id: 10, name: 'ขาตั้งโทรศัพท์', price: 350, category: 'mobile', stock: 0 },
]

//คล้ายกับ for loop แต่สามารถคืนค่าเป็น Array ใหม่ได้
const names = products.map((p) => p.name);
console.log(names);

const cheap = products.filter((p) => p.price < 1000);
console.log(cheap);

const found = products.find((p) => p.id === 5);
console.log(found);

const total = products.reduce((sum, p) => sum + p.price, 0);
console.log(total);

// some: มีอย่างน้อย 1 ตัวที่ตรงเงื่อนไขหรือไม่
const hasOutOfStock = products.some((p) => p.stock === 0);
console.log('some (มีสินค้าหมดไหม) ->', hasOutOfStock);

// ต่อกันเป็น Chain: ชื่อสินค้าหมวด accessories เรียงราคาจากน้อยไปมาก
const accessories = products
  .filter((p) => p.category === 'accessories')
  .toSorted((a, b) => b.price - a.price) //a-b = น้อยไปมาก, b-a = มากไปน้อย
  .map((p) => `${p.name} (${p.price})`);
console.log('chain :', accessories);