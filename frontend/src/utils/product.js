// Pure Function: รับข้อมูลเข้า คืนผลลัพธ์ใหม่ ไม่แก้ข้อมูลเดิม (ทดสอบง่ายในวันที่ 5)
export function filterProducts(list, keyword = '', category = 'all') {
  const q = keyword.trim().toLowerCase()
  return list.filter((p) => {
    const matchKeyword = !q || p.name.toLowerCase().includes(q)
    const matchCategory = category === 'all' || p.category?.slug === category
    return matchKeyword && matchCategory
  })
}