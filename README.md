# eDS — SNE eDocument System PWA

ระบบ Progressive Web App (PWA) สำหรับ eDS รองรับการใช้งานบน **Android · iOS · Desktop**

---

## 📁 โครงสร้างไฟล์

```
📦 eDS-pwa/
 ┣ 📄 index.html       ← หน้าหลัก (wrapper + PWA logic)
 ┣ 📄 manifest.json    ← PWA Manifest
 ┣ 📄 sw.js            ← Service Worker (cache + offline)
 ┣ 🖼️ icon.svg         ← Icon เวกเตอร์ (ทุกขนาด)
 ┣ 🖼️ icon-192.png     ← Icon 192×192 px
 ┣ 🖼️ icon-512.png     ← Icon 512×512 px
 ┗ 📄 README.md        ← ไฟล์นี้
```

---

## 🚀 วิธี Deploy บน GitHub Pages

1. สร้าง Repository ใหม่บน GitHub (เช่น `eDS-app`)
2. อัปโหลดไฟล์ทั้งหมดเข้า Repository
3. ไปที่ **Settings → Pages → Source → main branch → / (root)**
4. รอสักครู่แล้วเข้าใช้งานที่ `https://<username>.github.io/<repo>/`

---

## 📱 คุณสมบัติ

| Feature | Android | iOS | Desktop |
|---|---|---|---|
| ติดตั้งบนหน้าจอหลัก | ✅ Auto prompt | ✅ คู่มือ Safari | ✅ Browser button |
| Splash screen | ✅ | ✅ | ✅ |
| Offline support | ✅ | ✅ | ✅ |
| แจ้งเตือน offline | ✅ | ✅ | ✅ |
| เต็มจอ (Standalone) | ✅ | ✅ | ✅ |

---

## ⚙️ เปลี่ยน URL ของ Web App

เปิดไฟล์ `index.html` แล้วเปลี่ยน URL ใน `<iframe src="...">` บรรทัดนี้:

```html
<iframe
  id="app"
  src="https://YOUR_APP_URL_HERE"   ← ← เปลี่ยนตรงนี้
  ...>
</iframe>
```

---

## 🎨 เปลี่ยนชื่อแอป / สีธีม

แก้ไขใน `manifest.json`:
```json
{
  "name": "ชื่อเต็มของแอป",
  "short_name": "ชื่อย่อ",
  "theme_color": "#1565C0",
  "background_color": "#0D47A1"
}
```

และใน `index.html` บรรทัด `<meta name="theme-color">` ให้ตรงกัน

---

## 📝 License

Internal use — SNE Organization
