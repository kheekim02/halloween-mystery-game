import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
img = Image.new("RGBA", (W, H), "#081426")
draw = ImageDraw.Draw(img)

# Fonts
font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
font_title = ImageFont.truetype(font_path, 26)
font_zone_name = ImageFont.truetype(font_path, 20)
font_code = ImageFont.truetype(font_path, 15)
font_desc = ImageFont.truetype(font_path, 13)
font_small = ImageFont.truetype(font_path, 11)

# Grid lines
grid_size = 24
for x in range(0, W, grid_size):
    draw.line([(x, 0), (x, H)], fill="#0f2545", width=1)
for y in range(0, H, grid_size):
    draw.line([(0, y), (W, y)], fill="#0f2545", width=1)

# Outer Blueprint border
pad = 20
draw.rectangle([(pad, pad), (W - pad, H - pad)], outline="#00d4ff", width=2)
draw.rectangle([(pad + 4, pad + 4), (W - pad - 4, H - pad - 4)], outline="#005588", width=1)

# Header Title Block
draw.rectangle([(pad + 12, pad + 12), (pad + 420, pad + 65)], fill="#081830", outline="#00d4ff", width=1)
draw.text((pad + 25, pad + 18), "루나 하우스(Luna House) 8F 현장 평면도", fill="#ffffff", font=font_title)
draw.text((pad + 25, pad + 46), "ARCHITECTURAL CRIME SCENE BLUEPRINT | SCALE 1:50", fill="#00d4ff", font=font_small)

# Header Legend
draw.rectangle([(W - pad - 340, pad + 12), (W - pad - 12, pad + 65)], fill="#081830", outline="#00d4ff", width=1)
draw.text((W - pad - 325, pad + 18), "사건 발생 일시: 10월 31일 오후 10:45", fill="#ffaa44", font=font_desc)
draw.text((W - pad - 325, pad + 38), "상태: 암전 이벤트 중 박서준 독살 발생 [수사 통제 구역]", fill="#ff4466", font=font_small)

# 6 Room Layout
zones = [
    {
        "code": "A-01",
        "name": "VIP 휴게실 [시신 발견지]",
        "rect": (40, 90, 520, 380),
        "border": "#ff3355",
        "fill": "#1f0d18",
        "text_color": "#ff4d6d",
        "desc": "• 박서준 시신 발견 (가죽 소파 앞 엎드림)\n• 원형 유리 테이블 위 칵테일 잔 & 블랙 해골 빨대\n• 황색 폴리스라인 설치 구역 [CRIME SCENE]",
        "accent": "CRIME SCENE",
        "symbol": "🛋️ SOFA & TABLE"
    },
    {
        "code": "B-02",
        "name": "바 카운터 & 마녀 솥",
        "rect": (540, 90, 940, 380),
        "border": "#ffaa00",
        "fill": "#1a1608",
        "text_color": "#ffbb33",
        "desc": "• 마녀 솥 칵테일 볼 (드라이아이스 연기)\n• 음료 셰이커, 크랜베리 시럽, 보드카 원액\n• 바 카운터 공용 스트라이프 종이 빨대 디스펜서",
        "accent": "BEVERAGE BAR",
        "symbol": "🍸 BAR COUNTER"
    },
    {
        "code": "C-03",
        "name": "루프탑 야외 테라스",
        "rect": (960, 90, 1240, 380),
        "border": "#bb55ff",
        "fill": "#160e24",
        "text_color": "#cc77ff",
        "desc": "• 도심 야경 조망 난간 구역\n• 바닥에 짓밟힌 김건희의 담배꽁초\n• 찢어진 방콕행 편도 비행기 티켓 조각",
        "accent": "OUTDOOR BALCONY",
        "symbol": "🌙 TERRACE DECK"
    },
    {
        "code": "F-06",
        "name": "안쪽 화장실",
        "rect": (40, 400, 320, 680),
        "border": "#00ddaa",
        "fill": "#081c1c",
        "text_color": "#33ffcc",
        "desc": "• 세면대, 대형 거울, 위생 설비\n• 도주현 구토 및 세수 알리바이 주장 장소\n• 화장실 선반 위 김유은 스마트폰 메모",
        "accent": "RESTROOM",
        "symbol": "🚻 WASHROOM"
    },
    {
        "code": "D-04",
        "name": "현관 복도 & 중문",
        "rect": (340, 400, 760, 680),
        "border": "#00bbee",
        "fill": "#09192e",
        "text_color": "#44ccff",
        "desc": "• 파티룸 출입 메인 양개문 및 신발장\n• 배달 음식 수령 중문 (조신영 통화 장소)\n• 복도 바닥에 튄 붉은 와인 자국 흔적",
        "accent": "ENTRANCE & HALLWAY",
        "symbol": "🚪 MAIN CORRIDOR"
    },
    {
        "code": "E-05",
        "name": "할로윈 포토존 & DJ 콘솔",
        "rect": (780, 400, 1240, 680),
        "border": "#3388ff",
        "fill": "#0b162e",
        "text_color": "#66aaff",
        "desc": "• 카메라 삼각대 & 안보영 핸드백 (위조 감정서)\n• 실내 조명 스위치 배전반 & BGM 블루투스 콘솔\n• 문지영의 파티 데코 소품 가방 (뜯긴 해골 빨대 팩)",
        "accent": "PHOTO & CONTROL",
        "symbol": "📸 PHOTO / DJ DESK"
    }
]

for z in zones:
    x1, y1, x2, y2 = z["rect"]
    # Background fill
    draw.rectangle([x1, y1, x2, y2], fill=z["fill"], outline=z["border"], width=2)
    # Inner border
    draw.rectangle([x1 + 4, y1 + 4, x2 - 4, y2 - 4], outline=z["border"] + "44", width=1)
    
    # Code badge
    draw.rectangle([x1 + 10, y1 + 10, x1 + 70, y1 + 34], fill="#08182b", outline=z["border"], width=1)
    draw.text((x1 + 18, y1 + 13), z["code"], fill=z["text_color"], font=font_code)
    
    # Accent tag
    draw.text((x1 + 80, y1 + 15), z["accent"], fill=z["text_color"] + "aa", font=font_small)
    
    # Room Name (Korean)
    draw.text((x1 + 12, y1 + 44), z["name"], fill="#ffffff", font=font_zone_name)
    
    # Symbol
    draw.text((x2 - 170, y1 + 15), z["symbol"], fill=z["text_color"] + "88", font=font_small)
    
    # Divider line
    draw.line([(x1 + 10, y1 + 75), (x2 - 10, y1 + 75)], fill=z["border"] + "55", width=1)
    
    # Bullet descriptions
    lines = z["desc"].split("\n")
    cur_y = y1 + 85
    for line in lines:
        draw.text((x1 + 14, cur_y), line, fill="#d0dbe5", font=font_desc)
        cur_y += 24

# Save blueprint
out_path = "/Users/geoffrey/.gemini/antigravity/scratch/halloween-mystery-game/blueprint.png"
img.save(out_path, "PNG")
print(f"Successfully generated Korean blueprint at {out_path}")
