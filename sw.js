//Service Worker (sw.js)
//สร้างไฟล์ชื่อ sw.js ไว้ที่ Root (ที่เดียวกับ index.html)
//ช่วยให้ Chrome ยอม "เด้ง" ปุ่มติดตั้ง (Install)
const CACHE_NAME = 'eds-cache-v1';
const urlsToCache = [
  '/eDS/',
  '/eDS/index.html',
  '/eDS/manifest.json',
  '/eDS/icon.png'
];

// ขั้นตอนการติดตั้ง (Install) - เก็บไฟล์ลง Cache
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// ขั้นตอนการดึงข้อมูล (Fetch) - ถ้ามีใน Cache ให้ดึงจาก Cache ถ้าไม่มีให้ดึงจาก Network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
