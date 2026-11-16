// ข้อมูลจำลองของ ShopMini (ใช้ในวันที่ 1-2 ก่อนเชื่อม API จริงในวันที่ 4)
export const categories = [
  { id: 1, slug: 'accessories', name: 'อุปกรณ์คอมพิวเตอร์' },
  { id: 2, slug: 'audio', name: 'เครื่องเสียง' },
  { id: 3, slug: 'mobile', name: 'อุปกรณ์มือถือ' },
  { id: 4, slug: 'office', name: 'ของใช้บนโต๊ะทำงาน' },
]

// ดึงหมวดหมู่ตาม slug (โครงสร้างเดียวกับที่ API ส่งกลับมาในวันที่ 4)
const cat = (slug) => categories.find((c) => c.slug === slug)

export const products = [
  { id: 1, name: 'เมาส์ไร้สาย Ergonomic', price: 590, category: cat('accessories'), stock: 25, image_url: 'https://picsum.photos/seed/shopmini-1/400/300', description: 'เมาส์ทรงตั้ง ลดอาการปวดข้อมือ เชื่อมต่อได้ทั้ง Bluetooth และ USB Receiver' },
  { id: 2, name: 'คีย์บอร์ด Mechanical TKL', price: 1890, category: cat('accessories'), stock: 12, image_url: 'https://picsum.photos/seed/shopmini-2/400/300', description: 'คีย์บอร์ดขนาด 87 ปุ่ม สวิตช์ Brown เสียงเบา เหมาะกับงานพิมพ์' },
  { id: 3, name: 'แผ่นรองเมาส์ XL', price: 290, category: cat('accessories'), stock: 40, image_url: 'https://picsum.photos/seed/shopmini-3/400/300', description: 'แผ่นรองขนาด 90 x 40 ซม. ขอบเย็บกันลุ่ย' },
  { id: 4, name: 'USB-C Hub 7-in-1', price: 1290, category: cat('accessories'), stock: 18, image_url: 'https://picsum.photos/seed/shopmini-4/400/300', description: 'HDMI 4K, USB-A 3 พอร์ต, SD Card และ PD 100W' },
  { id: 5, name: 'หูฟังบลูทูธ ANC', price: 2490, category: cat('audio'), stock: 10, image_url: 'https://picsum.photos/seed/shopmini-5/400/300', description: 'ตัดเสียงรบกวน ใช้งานต่อเนื่อง 30 ชั่วโมง' },
  { id: 6, name: 'ลำโพงพกพากันน้ำ', price: 1590, category: cat('audio'), stock: 15, image_url: 'https://picsum.photos/seed/shopmini-6/400/300', description: 'มาตรฐาน IPX7 เสียงเบสแน่น พกไปเที่ยวได้' },
  { id: 7, name: 'ไมโครโฟน USB สำหรับประชุม', price: 1990, category: cat('audio'), stock: 8, image_url: 'https://picsum.photos/seed/shopmini-7/400/300', description: 'รับเสียงรอบทิศทาง เสียบใช้งานได้ทันที' },
  { id: 8, name: 'สายชาร์จ USB-C 2 เมตร', price: 250, category: cat('mobile'), stock: 60, image_url: 'https://picsum.photos/seed/shopmini-8/400/300', description: 'สายถักไนลอน รองรับชาร์จเร็ว 60W' },
  { id: 9, name: 'พาวเวอร์แบงก์ 20000mAh', price: 990, category: cat('mobile'), stock: 22, image_url: 'https://picsum.photos/seed/shopmini-9/400/300', description: 'ชาร์จเร็ว PD 22.5W พร้อมจอแสดงแบตเตอรี่' },
  { id: 10, name: 'ขาตั้งโทรศัพท์ตั้งโต๊ะ', price: 350, category: cat('mobile'), stock: 0, image_url: 'https://picsum.photos/seed/shopmini-10/400/300', description: 'ปรับมุมได้ 270 องศา วัสดุอะลูมิเนียม' },
  { id: 11, name: 'โคมไฟตั้งโต๊ะ LED', price: 890, category: cat('office'), stock: 14, image_url: 'https://picsum.photos/seed/shopmini-11/400/300', description: 'ปรับความสว่างและอุณหภูมิสีได้ 5 ระดับ' },
  { id: 12, name: 'ขาตั้งแล็ปท็อปอะลูมิเนียม', price: 790, category: cat('office'), stock: 20, image_url: 'https://picsum.photos/seed/shopmini-12/400/300', description: 'ยกจอให้อยู่ระดับสายตา พับเก็บได้' },
]