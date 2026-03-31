# eDS — SNE-eDocument PWA 🟢

> ระบบเอกสารอิเล็กทรอนิกส์ SNE | Progressive Web App  
> สีธีม: เขียว Fresh/Modern | รองรับ Android · iOS · Desktop

---

## 📁 โครงสร้างไฟล์

```
eDS-PWA/
├── index.html       ← หน้าหลัก (Splash + Loading + iframe + Install Banner)
├── manifest.json    ← PWA config
├── sw.js            ← Service Worker (offline cache)
└── icons/
    ├── icon.svg     ← ต้นฉบับ SVG
    ├── icon-16.png  … icon-512.png  (ทุกขนาด)
```

---

## 🚀 วิธีติดตั้งบน GitHub Pages

| ขั้นตอน | รายละเอียด |
|--------|------------|
| **1** | สร้าง Repository ใหม่ (Public) |
| **2** | Upload ไฟล์ทั้งหมดรวมถึงโฟลเดอร์ `icons/` |
| **3** | `Settings → Pages → Source: main → / (root)` |
| **4** | รอ ~2 นาที → เข้าใช้ที่ `https://[user].github.io/[repo]/` |

---

## 🔗 เปลี่ยน URL ของแอป

เปิด `index.html` แก้บรรทัด:

```html
<iframe
  id="app"
  src="YOUR_URL_HERE"   ← แก้ตรงนี้
```

---

## 📱 วิธีติดตั้งบนมือถือ

**Android** → Chrome จะแสดง Banner "ติดตั้ง" อัตโนมัติ  
**iOS** → Safari → Share (□↑) → Add to Home Screen  
**Desktop** → กดไอคอน ⊕ ในแถบ Address Bar

---

## ✅ Features

- 🎨 Splash Screen พร้อม animated blobs + logo pulse
- ⚡ Custom loading bar + dots animation + cycling text
- 📲 Android Install Banner (auto-prompt)
- 🍎 iOS Install Step Guide (3 ขั้นตอน)
- 📶 Offline fallback ผ่าน Service Worker
- 🌙 Dark mode support
- 📐 Full-screen standalone mode (ไม่มี browser chrome)

---

Made for SNE 🟢
