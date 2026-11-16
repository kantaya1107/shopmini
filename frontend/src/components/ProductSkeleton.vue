<template>
  <!-- โครงร่างขนาดเท่าการ์ดจริง ทำให้หน้าไม่กระตุกเมื่อข้อมูลมาถึง -->
  <div class="animate-pulse overflow-hidden rounded-xl border border-slate-200 bg-white">
    <div class="aspect-4/3 w-full bg-slate-200"></div>
    <div class="flex flex-col gap-3 p-4">
      <div class="h-4 w-20 rounded bg-slate-200"></div>
      <div class="h-4 w-3/4 rounded bg-slate-200"></div>
      <div class="h-5 w-1/3 rounded bg-slate-200"></div>
      <div class="h-9 w-full rounded-lg bg-slate-200"></div>
    </div>
  </div>
</template>