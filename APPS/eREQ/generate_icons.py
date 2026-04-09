#!/usr/bin/env python3 Generate by AI
"""
Generate all PWA icon sizes for eREQ from SVG source.
Run: python3 generate_icons.py
Requires: pip install cairosvg pillow
"""

import os

# SVG source - eREQ logo
SVG_CONTENT = '''<svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="512" height="512" rx="96" fill="url(#bg)"/>
  
  <!-- Document shape -->
  <rect x="80" y="60" width="280" height="340" rx="24" fill="url(#doc)" filter="url(#shadow)"/>
  
  <!-- Folded corner -->
  <path d="M280 60 L360 60 L360 140 Z" fill="rgba(0,0,0,0.2)"/>
  <path d="M280 60 L280 140 L360 140" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="3"/>
  
  <!-- Lines on document -->
  <rect x="112" y="200" width="216" height="16" rx="8" fill="white" opacity="0.9"/>
  <rect x="112" y="236" width="216" height="16" rx="8" fill="white" opacity="0.75"/>
  <rect x="112" y="272" width="160" height="16" rx="8" fill="white" opacity="0.6"/>
  <rect x="112" y="308" width="200" height="16" rx="8" fill="white" opacity="0.45"/>
  
  <!-- "e" badge circle -->
  <circle cx="360" cy="380" r="100" fill="url(#gold)" filter="url(#glow)"/>
  
  <!-- "e" letter -->
  <text x="360" y="420" 
        text-anchor="middle" 
        fill="white" 
        font-size="110" 
        font-weight="800" 
        font-family="Georgia, serif"
        letter-spacing="-2">e</text>
  
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e4d8c"/>
      <stop offset="100%" stop-color="#0f2540"/>
    </linearGradient>
    <linearGradient id="doc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#3a8fd4"/>
      <stop offset="100%" stop-color="#1a5a9c"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f5b800"/>
      <stop offset="100%" stop-color="#d48c00"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="4" dy="8" stdDeviation="12" flood-opacity="0.3"/>
    </filter>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#f5b800" flood-opacity="0.4"/>
    </filter>
  </defs>
</svg>'''

SIZES = [16, 32, 72, 96, 128, 144, 152, 192, 384, 512]

def generate_icons():
    os.makedirs('icons', exist_ok=True)
    
    # Save SVG source
    with open('icons/icon.svg', 'w') as f:
        f.write(SVG_CONTENT)
    print("✅ Saved icons/icon.svg")
    
    # Try cairosvg first
    try:
        import cairosvg
        for size in SIZES:
            output_path = f'icons/icon-{size}.png'
            cairosvg.svg2png(
                bytestring=SVG_CONTENT.encode(),
                write_to=output_path,
                output_width=size,
                output_height=size
            )
            print(f"✅ Generated {output_path} ({size}x{size})")
        print("\n🎉 All icons generated successfully!")
        return True
    except ImportError:
        print("⚠️  cairosvg not found. Trying Pillow fallback...")
    
    # Pillow fallback (creates placeholder colored icons)
    try:
        from PIL import Image, ImageDraw, ImageFont
        for size in SIZES:
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Background with rounded corners
            margin = size // 16
            draw.rounded_rectangle(
                [margin, margin, size-margin, size-margin],
                radius=size//6,
                fill=(26, 58, 92, 255)  # navy
            )
            
            # Gold circle
            cx, cy = int(size*0.7), int(size*0.7)
            r = int(size*0.22)
            draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(240, 165, 0, 255))
            
            # "e" text
            font_size = int(size * 0.25)
            try:
                font = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf', font_size)
            except:
                font = ImageFont.load_default()
            draw.text((cx, cy), 'e', fill=(255,255,255,255), font=font, anchor='mm')
            
            output_path = f'icons/icon-{size}.png'
            img.save(output_path, 'PNG')
            print(f"✅ Generated {output_path} ({size}x{size})")
        
        print("\n🎉 All icons generated with Pillow!")
        print("💡 For higher quality icons, install cairosvg: pip install cairosvg")
        return True
    except ImportError:
        print("❌ Pillow also not found.")
        print("Install with: pip install cairosvg pillow")
        return False

if __name__ == '__main__':
    print("🚀 Generating eREQ PWA icons...\n")
    generate_icons()
    print("\n📁 Icons saved to ./icons/ folder")
