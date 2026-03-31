# eDS — SNE Electronic Document System (PWA)

> ระบบเอกสารอิเล็กทรอนิกส์ SNE แบบ Progressive Web App  
> รองรับ Android · iOS · Desktop

---

## 📁 โครงสร้างไฟล์

```
eDS-PWA/
├── index.html          ← หน้าหลัก (Splash, iframe, install banner)
├── manifest.json       ← PWA manifest (ชื่อแอป, ไอคอน, สี)
├── sw.js               ← Service Worker (offline, caching)
├── generate_icons.py   ← สคริปต์สร้างไอคอนอัตโนมัติ
└── icons/
    ├── icon.svg        ← ไอคอนต้นฉบับ (SVG)
    ├── icon-16.png
    ├── icon-32.png
    ├── icon-72.png
    ├── icon-96.png
    ├── icon-128.png
    ├── icon-144.png
    ├── icon-152.png
    ├── icon-192.png    ← ใช้สำหรับ Android Home Screen
    ├── icon-384.png
    └── icon-512.png    ← ใช้สำหรับ Splash Screen / Store
```

---

## 🚀 วิธีติดตั้งบน GitHub Pages

### 1. สร้าง Repository ใหม่
```
Repository name: eds-app  (หรือชื่ออื่นก็ได้)
Visibility: Public
```

### 2. อัปโหลดไฟล์ทั้งหมด
```
drag & drop ไฟล์ทุกไฟล์ + โฟลเดอร์ icons/ เข้าไปใน repository
```

### 3. เปิด GitHub Pages
```
Settings → Pages → Source: Deploy from branch → main → / (root)
```

### 4. รอประมาณ 1-2 นาที แล้วเข้าใช้ที่:
```
https://[username].github.io/[repo-name]/
```

---

## 📱 การติดตั้งบนมือถือ

### Android (Chrome)
- เปิดเว็บในแอป Chrome
- กดปุ่ม **"ติดตั้ง"** ที่แถบด้านล่าง
- หรือกด ⋮ → "Add to Home Screen"

### iOS (Safari)
- เปิดเว็บในแอป **Safari** (ต้องเป็น Safari เท่านั้น)
- กดปุ่ม **Share** (□↑) ที่แถบด้านล่าง
- เลือก **"Add to Home Screen"**

### Desktop (Chrome/Edge)
- กดไอคอน ⊕ ในแถบ URL
- หรือเมนู → "Install app"

---

## 🔧 การแก้ไข URL ของแอป

เปิดไฟล์ `index.html` และแก้ไข `src` ใน iframe:

```html
<iframe
  id="app"
  src="YOUR_APP_URL_HERE"   ← ← ← แก้ตรงนี้
  ...
```

---

## 🎨 การเปลี่ยนสีธีม

แก้ไข CSS variables ใน `index.html`:

```css
:root {
  --navy: #1a3a5c;        /* สีหลัก */
  --accent: #2a7fd4;      /* สีเน้น */
  --gold: #f0a500;        /* สีทอง (badge) */
}
```

และในไฟล์ `manifest.json`:
```json
"theme_color": "#1a3a5c",
"background_color": "#0f2540"
```

---

## ✏️ การสร้างไอคอนใหม่

1. แก้ไข SVG ใน `generate_icons.py` (ตัวแปร `SVG_CONTENT`)
2. รันสคริปต์:
   ```bash
   pip install cairosvg pillow
   python3 generate_icons.py
   ```
3. อัปโหลดโฟลเดอร์ `icons/` ขึ้น GitHub ใหม่

---

## ✅ Features

| Feature | Android | iOS | Desktop |
|---------|---------|-----|---------|
| Splash Screen | ✅ | ✅ | ✅ |
| Install Banner | ✅ | ✅ (guide) | ✅ |
| Home Screen Icon | ✅ | ✅ | ✅ |
| Offline Fallback | ✅ | ✅ | ✅ |
| Dark Mode | ✅ | ✅ | ✅ |
| Full Screen Mode | ✅ | ✅ | ✅ |

---

Made with ❤️ for SNE
