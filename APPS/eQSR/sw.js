// eQSR service worker: โหลดจากเครือข่ายก่อนเสมอ (ไม่ใช้แคชเก่า) ใช้แคชเฉพาะตอนออฟไลน์
var CACHE = 'eqsr-v2';
self.addEventListener('install', function () { self.skipWaiting(); });
self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (ks) {
      return Promise.all(ks.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});
self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;                    // POST (Apps Script API) ผ่านตรง
  var url = new URL(req.url);
  if (url.origin !== location.origin) return;          // CDN / Google Drive / Fonts ผ่านตรง
  e.respondWith(
    fetch(req, { cache: 'no-store' }).then(function (res) {
      if (res && res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(url.pathname, copy); }); }
      return res;
    }).catch(function () {
      return caches.match(url.pathname).then(function (r) { return r || caches.match('app.html'); });
    })
  );
});
