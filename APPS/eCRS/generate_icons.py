#!/usr/bin/env python3
"""
Generate all PWA icon sizes for eCRS from SVG source.
สีแดงเลือดนก + ข้อความ eCRS
"""

import os
import cairosvg

SVG_CONTENT = '''<svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">

  <!-- Background gradient: สีแดงเลือดนก -->
  <rect width="512" height="512" rx="96" fill="url(#bg)"/>

  <!-- Document shape (เล็กลงนิดเพื่อให้มีที่ข้อความด้านล่าง) -->
  <rect x="90" y="44" width="260" height="300" rx="22" fill="url(#doc)" filter="url(#shadow)"/>

  <!-- Folded corner -->
  <path d="M270 44 L350 44 L350 118 Z" fill="rgba(0,0,0,0.25)"/>
  <path d="M270 44 L270 118 L350 118" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="3"/>

  <!-- Lines on document -->
  <rect x="118" y="168" width="204" height="13" rx="6" fill="white" opacity="0.90"/>
  <rect x="118" y="198" width="204" height="13" rx="6" fill="white" opacity="0.75"/>
  <rect x="118" y="228" width="152" height="13" rx="6" fill="white" opacity="0.60"/>
  <rect x="118" y="258" width="185" height="13" rx="6" fill="white" opacity="0.45"/>

  <!-- "e" badge circle -->
  <circle cx="350" cy="330" r="88" fill="url(#gold)" filter="url(#glow)"/>

  <!-- "e" letter in badge -->
  <text x="350" y="368"
        text-anchor="middle"
        fill="white"
        font-size="98"
        font-weight="800"
        font-family="Georgia, serif"
        letter-spacing="-2">e</text>

  <!-- eCRS label ด้านล่าง -->
  <rect x="28" y="424" width="456" height="68" rx="16" fill="url(#label_bg)" opacity="0.92"/>
  <text x="256" y="474"
        text-anchor="middle"
        fill="white"
        font-size="52"
        font-weight="900"
        font-family="Arial Black, Arial, sans-serif"
        letter-spacing="4">eCRS</text>

  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#7A0000"/>
      <stop offset="100%" stop-color="#2E0000"/>
    </linearGradient>
    <linearGradient id="doc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#B03030"/>
      <stop offset="100%" stop-color="#7A1010"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#E8A000"/>
      <stop offset="100%" stop-color="#B87000"/>
    </linearGradient>
    <!-- แถบ eCRS ด้านล่าง: ดำแดงเข้ม -->
    <linearGradient id="label_bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#4A0000"/>
      <stop offset="50%"  stop-color="#6B0000"/>
      <stop offset="100%" stop-color="#4A0000"/>
    </linearGradient>

    <filter id="shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="4" dy="8" stdDeviation="12" flood-opacity="0.35"/>
    </filter>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#E8A000" flood-opacity="0.5"/>
    </filter>
  </defs>
</svg>'''

SIZES = [16, 32, 72, 96, 128, 144, 152, 192, 384, 512]

def generate_icons():
    os.makedirs('icons_ecrs_v2', exist_ok=True)

    with open('icons_ecrs_v2/icon.svg', 'w') as f:
        f.write(SVG_CONTENT)
    print("✅ Saved icons_ecrs_v2/icon.svg")

    for size in SIZES:
        output_path = f'icons_ecrs_v2/icon-{size}.png'
        cairosvg.svg2png(
            bytestring=SVG_CONTENT.encode(),
            write_to=output_path,
            output_width=size,
            output_height=size
        )
        print(f"✅ Generated {output_path}  ({size}x{size})")

    print("\n🎉 All eCRS icons (with text) generated successfully!")

if __name__ == '__main__':
    print("🚀 Generating eCRS PWA icons v2 (with eCRS text)...\n")
    generate_icons()
    print("\n📁 Icons saved to ./icons_ecrs_v2/ folder")
