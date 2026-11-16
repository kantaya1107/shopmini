<template>
  <div class="grid gap-6 md:grid-cols-[200px_1fr]">
    <aside class="h-fit rounded-xl border bg-white p-4">
      <p class="mb-3 font-semibold">เมนูผู้ดูแลระบบ</p>
      <nav class="flex flex-col gap-1 text-sm">
        <RouterLink :to="{ name: 'admin' }" exact-active-class="bg-brand-50 text-brand-700" class="rounded px-3 py-2">ภาพรวม</RouterLink>
        <RouterLink :to="{ name: 'admin-products' }" active-class="bg-brand-50 text-brand-700" class="rounded px-3 py-2">จัดการสินค้า</RouterLink>
      </nav>
    </aside>
    <!-- RouterView ชั้นในสำหรับ children ของ /admin -->
    <section><RouterView /></section>
  </div>
</template>