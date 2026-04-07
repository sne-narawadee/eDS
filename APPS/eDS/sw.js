const SHELL = [
  './index.html', './manifest.json',
  './icons/icon-192.png', './icons/icon-512.png'
];

let CACHE = 'eDS-init';

self.addEventListener('install', e => {
  e.waitUntil(
    // ดึง sw.js ตัวเองมา hash → ได้ cache name ที่ unique ทุกครั้งที่ไฟล์เปลี่ยน
    fetch('./sw.js?t=' + Date.now())
      .then(r => r.text())
      .then(text => crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)))
      .then(buf => {
        const hash = Array.from(new Uint8Array(buf))
          .slice(0, 4)
          .map(b => b.toString(16).padStart(2, '0'))
          .join('');
        CACHE = 'eDS-' + hash; // เช่น eDS-a3f2c1b0
      })
      .then(() => caches.open(CACHE).then(c => c.addAll(SHELL)))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if (!e.request.url.startsWith('http')) return;

  const isHTML = e.request.mode === 'navigate' ||
                 e.request.url.endsWith('/') ||
                 e.request.url.includes('index.html');

  if (isHTML) {
    // HTML ดึง network ก่อนเสมอ ไม่ติดแคช
    e.respondWith(
      fetch(e.request)
        .then(res => {
          if (res && res.status === 200)
            caches.open(CACHE).then(c => c.put(e.request, res.clone()));
          return res;
        })
        .catch(() => caches.match('./index.html'))
    );
    return;
  }

  // Assets อื่น cache-first
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(res => {
        if (res && res.status === 200 && res.type !== 'opaque')
          caches.open(CACHE).then(c => c.put(e.request, res.clone()));
        return res;
      });
    })
  );
});
