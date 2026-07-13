/* if update code into index.html then change version this code */
const CACHE = 'eDS-v9';
/*-------------------------------------------------------------*/
const SHELL = ['./', './index.html', './manifest.json', './icons/icon-192.png', './icons/icon-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim())
  );
});
self.addEventListener('fetch', e => {
  if (!e.request.url.startsWith('http')) return;

  // ── แก้บั๊ก: เดิม SW ดักจับทุก origin รวมถึง script.google.com ด้วย ทำให้ ──
  // ── แคชหน้ารายงาน (ข้อมูล dynamic) ทับของเก่าไว้ และตอน fetch ล้มเหลวก็เอา ──
  // ── index.html (app shell) มาใส่แทนเนื้อหาจริงของ iframe ย่อย ทำให้หน้าจอ ──
  // ── ขาว/ดำ โดยไม่มี error ── ปล่อยผ่านคำขอข้าม origin ให้เบราว์เซอร์จัดการ ──
  // ── โดยตรง ไม่ต้องผ่าน SW เลย ──
  const url = new URL(e.request.url);
  if (url.origin !== self.location.origin) return;

  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(res => {
        if (res && res.status === 200 && res.type !== 'opaque') {
          const clone = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
        }
        return res;
      }).catch(() => e.request.mode === 'navigate' ? caches.match('./index.html') : undefined);
    })
  );
});
