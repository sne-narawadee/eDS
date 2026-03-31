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

#ติดตั้ง Python และ library ที่จำเป็น

1
เปิด Terminal (Mac/Linux) หรือ Command Prompt (Windows) แล้วรันคำสั่ง
pip install pillow cairosvg
ถ้าติดตั้ง cairosvg ไม่ได้ ใช้แค่ pillow ก็พอ — script รองรับทั้ง 2 แบบ

2
จัด folder ให้ถูกต้อง
ไฟล์ที่ต้องมีใน folder เดียวกันก่อนรัน
eDS-PWA/
├── generate_icons.py ← script ที่จะรัน
├── index.html
├── manifest.json
├── sw.js
└── icons/ ← จะสร้างให้อัตโนมัติ

3
แก้ไข SVG ในไฟล์ generate_icons.py
เปิดไฟล์ด้วย Notepad / VS Code แล้วหาตัวแปร SVG_CONTENT แก้ได้ตามต้องการ
# แก้ SVG ตรงนี้ — เปลี่ยนสี shape ข้อความได้เลย 
SVG_CONTENT = '''<svg viewBox="0 0 512 512"> <rect width="512" height="512" rx="96" fill="#1a3a5c"/> 
<!-- สีพื้นหลัง --> ... <text ...>eDS</text> <!-- ข้อความ --> </svg>'''
ถ้าไม่ถนัด SVG → ใช้ Figma/Canva ออกแบบแล้ว export เป็น SVG แปะแทนได้เลย

4
รัน script
เปิด Terminal แล้ว cd เข้าไปใน folder โปรเจกต์ จากนั้นรัน
# เข้าไปใน folder cd path/to/eDS-PWA # รัน script python generate_icons.py

5
ตรวจสอบผลลัพธ์
ถ้าสำเร็จจะเห็นข้อความ และไฟล์ใน icons/ ครบทุกขนาด
✅ icon-16.png ✅ icon-32.png ✅ icon-192.png ✅ icon-512.png ... 🎉 All icons generated!
6
อัปโหลดโฟลเดอร์ icons/ ขึ้น GitHub
ลาก folder icons/ ทั้งหมดไป drop ใน repository บน GitHub แล้วกด Commit changes
ทุกครั้งที่แก้ไขโลโก้ รัน script ใหม่ แล้วอัปโหลด icons/ ขึ้น GitHub อีกครั้ง — service worker จะ cache ใหม่ให้อัตโนมัติ

สรุปสั้นๆ ครับ — ทั้งหมดมี 6 ขั้นตอน:

1. ติดตั้ง `pip install pillow cairosvg`
2. จัด folder ให้ `generate_icons.py` อยู่ใน folder เดียวกับ `index.html`
3. เปิดไฟล์แก้ SVG ในตัวแปร `SVG_CONTENT` (เปลี่ยนสี, รูปทรง, ข้อความได้)
4. รัน `python generate_icons.py`
5. ตรวจสอบว่าได้ไฟล์ใน `icons/` ครบ
6. อัปโหลด folder `icons/` ขึ้น GitHub

ถ้าต้องการเปลี่ยนแค่สีพื้นหลังของไอคอน แก้แค่ค่า hex ใน `fill="..."` บรรทัดแรกของ SVG ก็พอครับ ไม่ต้องแก้อะไรเพิ่ม

---

## จุดที่แก้บ่อยที่สุด:
ต้องการเปลี่ยน                               แก้ที่
สีพื้นหลัง                                   stop-color ใน id="bg"
สีเอกสาร                                   stop-color ใน id="doc"
สีวงกลม badge                             stop-color ใน id="badge"
ข้อความ                                   >eDS< ใน <text>
ขนาดมุมโค้ง                                rx="96" ในบรรทัดพื้นหลัง

## ตัวอย่างถ้าอยากเปลี่ยนเป็น โทนเขียว แค่แก้ 2 บรรทัดนี้:
<stop offset="0%" stop-color="#06b06a"/>   # เขียวสว่าง
<stop offset="100%" stop-color="#054d31"/>  # เขียวเข้ม

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


## Code Sample

SVG_CONTENT = '''<svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">

  <!-- พื้นหลังโค้งมน (เปลี่ยน fill เพื่อเปลี่ยนสีพื้นหลัง) -->
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#2a6fd4"/>
      <stop offset="100%" stop-color="#0f2540"/>
    </linearGradient>
    <linearGradient id="doc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#5090e8"/>
      <stop offset="100%" stop-color="#2a5cb8"/>
    </linearGradient>
    <linearGradient id="badge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#5aaeff"/>
      <stop offset="100%" stop-color="#2a7fd4"/>
    </linearGradient>
  </defs>

  <!-- พื้นหลัง -->
  <rect width="512" height="512" rx="96" fill="url(#bg)"/>

  <!-- เอกสาร (document card) -->
  <rect x="72" y="62" width="276" height="348" rx="20" fill="url(#doc)" opacity="0.9"/>

  <!-- มุมพับ (dog-ear) -->
  <path d="M208 62 L348 62 L348 152 Z" fill="rgba(0,0,0,0.2)"/>
  <path d="M208 62 L208 152 L348 152" fill="none"
        stroke="rgba(255,255,255,0.15)" stroke-width="2"/>

  <!-- เส้นเนื้อหาในเอกสาร -->
  <rect x="104" y="226" width="210" height="18" rx="9"
        fill="white" opacity="0.90"/>
  <rect x="104" y="264" width="210" height="18" rx="9"
        fill="white" opacity="0.72"/>
  <rect x="104" y="302" width="148" height="18" rx="9"
        fill="white" opacity="0.55"/>
  <rect x="104" y="340" width="185" height="18" rx="9"
        fill="white" opacity="0.38"/>

  <!-- วงกลม badge มุมขวาล่าง -->
  <circle cx="356" cy="372" r="108" fill="url(#badge)"/>

  <!-- ตัวอักษร eDS (เปลี่ยน fill เพื่อเปลี่ยนสีตัวอักษร) -->
  <text x="356" y="420"
        text-anchor="middle"
        fill="white"
        font-size="118"
        font-weight="800"
        font-family="Arial, Helvetica, sans-serif">eDS</text>

</svg>'''
