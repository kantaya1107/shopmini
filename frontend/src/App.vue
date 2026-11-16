<script setup>
import AppNavbar from '@/components/AppNavbar.vue'
</script>

<template>
    <AppNavbar />
    <main class="mx-auto max-w-6xl px-4 py-6">
        <RouterView />
    </main>
</template>
