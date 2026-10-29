import os
from PIL import Image, ImageDraw, ImageFont

CLUES_DIR = "/Users/geoffrey/.gemini/antigravity/scratch/halloween-mystery-game/clues"
os.makedirs(CLUES_DIR, exist_ok=True)

font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
font_icon = ImageFont.truetype(font_path, 120)
font_num = ImageFont.truetype(font_path, 22)

# Clue 01 is already pure AI photo from subagent (clue_01.png).
# Generate pure visual cards for 02 to 14 without any rendered text inside
pure_clues = [
    {"id": "clue_02", "num": "02", "icon": "🍸", "accent": "#ffaa00", "glow": "#ff8800"},
    {"id": "clue_03", "num": "03", "icon": "🧪", "accent": "#00d4ff", "glow": "#0088cc"},
    {"id": "clue_04", "num": "04", "icon": "✈️", "accent": "#bb55ff", "glow": "#8822cc"},
    {"id": "clue_05", "num": "05", "icon": "⌚", "accent": "#ff8800", "glow": "#cc5500"},
    {"id": "clue_06", "num": "06", "icon": "👛", "accent": "#44aaff", "glow": "#1177cc"},
    {"id": "clue_07", "num": "07", "icon": "👔", "accent": "#ff4466", "glow": "#cc1133"},
    {"id": "clue_08", "num": "08", "icon": "✨", "accent": "#ff3355", "glow": "#dd1133"},
    {"id": "clue_09", "num": "09", "icon": "📑", "accent": "#ff0033", "glow": "#aa0022"},
    {"id": "clue_10", "num": "10", "icon": "🛍️", "accent": "#ff0033", "glow": "#aa0022"},
    {"id": "clue_11", "num": "11", "icon": "🎙️", "accent": "#bb55ff", "glow": "#8822cc"},
    {"id": "clue_12", "num": "12", "icon": "💬", "accent": "#44ccff", "glow": "#1188cc"},
    {"id": "clue_13", "num": "13", "icon": "📝", "accent": "#00ddaa", "glow": "#00aa77"},
    {"id": "clue_14", "num": "14", "icon": "🥤", "accent": "#ffaa00", "glow": "#cc7700"}
]

W, H = 500, 500

for c in pure_clues:
    img = Image.new("RGBA", (W, H), "#070e1b")
    draw = ImageDraw.Draw(img)

    # Grid
    for x in range(0, W, 25):
        draw.line([(x, 0), (x, H)], fill="#0c182c", width=1)
    for y in range(0, H, 25):
        draw.line([(0, y), (W, y)], fill="#0c182c", width=1)

    # Ambient radial spotlight
    draw.ellipse([80, 80, 420, 420], fill="#0f223d", outline=None)
    draw.ellipse([130, 130, 370, 370], fill="#132a4a", outline=c["accent"], width=2)
    draw.ellipse([145, 145, 355, 355], fill="#0a1728", outline=c["glow"], width=1)

    # Outer decorative frame
    draw.rectangle([(16, 16), (W - 16, H - 16)], outline="#1b3558", width=2)
    draw.rectangle([(20, 20), (W - 20, H - 20)], outline="#0f223a", width=1)

    # Corner brackets
    corner_len = 28
    corners = [(20, 20), (W - 20, 20), (20, H - 20), (W - 20, H - 20)]
    for cx, cy in corners:
        dx = corner_len if cx == 20 else -corner_len
        dy = corner_len if cy == 20 else -corner_len
        draw.line([(cx, cy), (cx + dx, cy)], fill=c["accent"], width=3)
        draw.line([(cx, cy), (cx, cy + dy)], fill=c["accent"], width=3)

    # Top Evidence Badge
    draw.rectangle([(28, 28), (140, 64)], fill="#081424", outline=c["accent"], width=1)
    draw.text((38, 33), f"CASE #{c['num']}", fill=c["accent"], font=font_num)

    # Center Visual Icon (Emoji/Forensic Object)
    bbox = draw.textbbox((0, 0), c["icon"], font=font_icon)
    icon_w = bbox[2] - bbox[0]
    icon_h = bbox[3] - bbox[1]
    draw.text(((W - icon_w) // 2, (H - icon_h) // 2 - 10), c["icon"], fill="#ffffff", font=font_icon)

    out_file = os.path.join(CLUES_DIR, f"{c['id']}.png")
    img.save(out_file, "PNG")

print("Created pure visual evidence graphics without text artifacts!")
