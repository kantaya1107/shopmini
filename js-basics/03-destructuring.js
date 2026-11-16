const product = {
  id: 5,
  name: "หูฟังบลูทูธ ANC",
  price: 2490,
  seller: { name: "Audio Pro", address: "Chonburi" },
};

console.log(product.name); //การเข้าถึง property ของ object แบบเดิม

//Destructuring
const { name, price, seller } = product;
console.log(name);
console.log(price);
console.log(seller.name);

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
console.log(array1 + array2); //การบวก array แบบนี้จะได้เป็น string "1,2,34,5,6" ไม่ใช่ array ใหม่
//... spread operator
console.log([...array1, ...array2]); //การรวม array แบบนี้จะได้เป็น array ใหม่ [1,2,3,4,5,6]
//optional chaining (?.) และ nullish coalescing operator (??)
console.log(product.seller?.address ?? "ที่อยู่ไม่ระบุ"); //การเข้าถึง property ของ object แบบ destructuring พร้อมกับการตรวจสอบค่า null หรือ undefined