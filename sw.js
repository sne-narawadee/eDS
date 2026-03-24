//Service Worker (sw.js)
//สร้างไฟล์ชื่อ sw.js ไว้ที่ Root (ที่เดียวกับ index.html)
//ช่วยให้ Chrome ยอม "เด้ง" ปุ่มติดตั้ง (Install)
// sw.js - Version: Network First (No Cache)
self.addEventListener('install', (event) => {
  // บังคับให้ Service Worker ตัวใหม่ทำงานทันที
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  // ควบคุมหน้าเว็บทั้งหมดทันทีที่ติดตั้งเสร็จ
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
  // ปล่อยให้ทุก Request วิ่งไปที่ Network โดยตรง ไม่ต้องเช็ก Cache
  event.respondWith(fetch(event.request));
});
