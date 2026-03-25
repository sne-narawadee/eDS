/* ============================================================
   eDS — Service Worker
   กลยุทธ์: Network First → Cache Fallback
   ============================================================ */

const CACHE_NAME   = 'eDS-shell-v1';
const SHELL_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './icon.svg'
];

/* ── Install: แคช App Shell ── */
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(SHELL_ASSETS))
      .then(() => self.skipWaiting())
  );
});

/* ── Activate: ลบ Cache เก่า ── */
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(k => k !== CACHE_NAME)
          .map(k => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

/* ── Fetch: Network First, ถ้า offline ใช้ Cache ── */
self.addEventListener('fetch', event => {
  const { request } = event;

  // ข้าม cross-origin requests (iframe content, Google APIs)
  if (!request.url.startsWith(self.location.origin)) return;

  event.respondWith(
    fetch(request)
      .then(response => {
        // อัปเดต cache ด้วยเวอร์ชันล่าสุด
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
        }
        return response;
      })
      .catch(() => caches.match(request))
  );
});
