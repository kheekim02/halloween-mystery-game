import os
from PIL import Image, ImageDraw, ImageFont

CLUES_DIR = "/Users/geoffrey/.gemini/antigravity/scratch/halloween-mystery-game/clues"
os.makedirs(CLUES_DIR, exist_ok=True)

font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
font_title = ImageFont.truetype(font_path, 28)
font_sub = ImageFont.truetype(font_path, 18)
font_code = ImageFont.truetype(font_path, 16)
font_meta = ImageFont.truetype(font_path, 13)
font_large_icon = ImageFont.truetype(font_path, 60)

clues_data = [
    {
        "id": "clue_01",
        "num": "01",
        "title": "박서준의 시신과 칵테일 잔",
        "zone": "VIP 휴게실 [시신 발견지]",
        "tag": "KEY EVIDENCE",
        "tag_color": "#ff3355",
        "icon": "💀",
        "details": [
            "• 박서준 시신 입술 검붉게 변색, 아몬드 향 검출",
            "• 원형 테이블 위 잔여 칵테일 잔 놓여 있음",
            "• 잔 속에서 독특한 '블랙 해골 플라스틱 빨대' 확인"
        ]
    },
    {
        "id": "clue_02",
        "num": "02",
        "title": "대형 펀치 볼과 칵테일 원액",
        "zone": "바 카운터 [음료 제조대]",
        "tag": "TOXICOLOGY: NEGATIVE",
        "tag_color": "#00ddaa",
        "icon": "🍸",
        "details": [
            "• 김유은이 제조한 크랜베리 시럽 & 보드카 원액",
            "• 마녀 솥 펀치 볼 내부 잔여 액체 간이 시약 반응",
            "• 감식 결과: [독극물 음성 (무독성 판정)]"
        ]
    },
    {
        "id": "clue_03",
        "num": "03",
        "title": "서준의 잔에 남은 칵테일 액체",
        "zone": "VIP 휴게실 [소파 테이블]",
        "tag": "MYSTERY NEGATIVE",
        "tag_color": "#ffaa00",
        "icon": "🧪",
        "details": [
            "• 서준이 마시던 유리잔 바닥 30ml 붉은 액체",
            "• 스포이트 정밀 채취 화학 반응 검사",
            "• 잔 속 '액체 자체'에서는 독극물 미검출!"
        ]
    },
    {
        "id": "clue_04",
        "num": "04",
        "title": "찢어진 편도 티켓과 담배꽁초",
        "zone": "루프탑 테라스 [야외 난간]",
        "tag": "PHYSICAL STRUGGLE",
        "tag_color": "#bb55ff",
        "icon": "✈️",
        "details": [
            "• 오늘 밤 오후 11:40 인천발 방콕행 편도 항공권",
            "• 서준 명의 출력본이 반으로 찢겨 난간 밑에 버려짐",
            "• 바닥에 김건희 피우는 담배 브랜드 꽁초 짓밟힘"
        ]
    },
    {
        "id": "clue_05",
        "num": "05",
        "title": "명품 시계 위조 감정서와 장부",
        "zone": "안보영의 핸드백 [포토존 의자]",
        "tag": "FRAUD EVIDENCE",
        "tag_color": "#ff8800",
        "icon": "⌚",
        "details": [
            "• 안보영의 3,500만 원 롤렉스 바꿔치기 모의 서류",
            "• 가짜 짝퉁 감정서 사본 및 일련번호 조작 장부",
            "• 안보영이 오늘 밤 서준의 가방에서 훔쳐낸 증거"
        ]
    },
    {
        "id": "clue_06",
        "num": "06",
        "title": "박서준의 명품 지갑과 현금 20만원",
        "zone": "권민호의 외투 [콘솔 옆 의자]",
        "tag": "THEFT ITEM",
        "tag_color": "#44aaff",
        "icon": "👛",
        "details": [
            "• 피해자 박서준의 악어가죽 반지갑과 신분증",
            "• 지갑에서 빼낸 5만 원권 현금 4장 민호 바지서 발견",
            "• 권민호의 단순 절도 혐의 입증 증거물"
        ]
    },
    {
        "id": "clue_07",
        "num": "07",
        "title": "도주현의 셔츠 깃 와인 & 까진 손",
        "zone": "현관 복도 [통로 구역]",
        "tag": "ALTERCATION",
        "tag_color": "#ff5555",
        "icon": "👔",
        "details": [
            "• 도주현 흰색 드레스 셔츠 깃에 묻은 붉은 와인 자국",
            "• 주현의 오른손 손등에 긁힌 생채기",
            "• 서준의 뜯겨진 와이셔츠 단추 1개와 일치"
        ]
    },
    {
        "id": "clue_08",
        "num": "08",
        "title": "초미세 면봉과 네일 글리터 공병",
        "zone": "문지영의 파우치 [포토존 선반]",
        "tag": "SUSPICIOUS RESIDUE",
        "tag_color": "#ff3355",
        "icon": "✨",
        "details": [
            "• 작은 유리 글리터 공병 틈새의 미세 백색 분말",
            "• 좁은 틈에 가루를 바르는 데 쓰인 초미세 면봉",
            "• 면봉 끝에 하얀 화학 잔여물 결정 흡착"
        ]
    },
    {
        "id": "clue_09",
        "num": "09",
        "title": "국과수 부검 속보 정밀 보고서",
        "zone": "국과수 긴급 감식 [2차 해금]",
        "tag": "SMOKING GUN #1",
        "tag_color": "#ff0033",
        "icon": "📑",
        "details": [
            "• 직접 사인: 급성 시안화칼륨(청산가리) 호흡 마비",
            "• 칵테일 액체는 무독성이었으나 치아/혀에서 독 검출",
            "• [블랙 해골 빨대 플라스틱 내부]와 [지영 공병] 독 일치!"
        ]
    },
    {
        "id": "clue_10",
        "num": "10",
        "title": "1개 빈 해골 빨대 팩과 영수증",
        "zone": "문지영 소품백 [포토존 바닥]",
        "tag": "SMOKING GUN #2",
        "tag_color": "#ff0033",
        "icon": "🛍️",
        "details": [
            "• 오늘 낮 파티샵 구매 '블랙 해골 스트로우 10개입' 팩",
            "• 비닐 상단이 정교하게 절개되어 9개만 남아있음",
            "• 사라진 단 1개의 빨대가 바로 서준의 잔에 꽂힌 것!"
        ]
    },
    {
        "id": "clue_11",
        "num": "11",
        "title": "테라스 실랑이 음성 녹음 파일",
        "zone": "김건희 스마트폰 [테라스 난간]",
        "tag": "AUDIO RECORDING",
        "tag_color": "#bb55ff",
        "icon": "🎙️",
        "details": [
            "• 오후 10:41 테라스 녹음: '파티 끝나면 경찰서 간다'",
            "• 서준이 살아서 사채를 갚아야 했으므로 살인 동기 반증",
            "• 건희는 서준의 해외 도주를 막으려던 것 확인"
        ]
    },
    {
        "id": "clue_12",
        "num": "12",
        "title": "박서준과의 마지막 독촉 문자",
        "zone": "조신영 스마트폰 [현관문 앞]",
        "tag": "SMS LOG",
        "tag_color": "#44ccff",
        "icon": "💬",
        "details": [
            "• 오후 10:21 카톡: '12시까지 100만 원 안 넣으면 고소'",
            "• 서준에게 돈을 돌려받으려 법적 고소를 준비함",
            "• 죽으면 대관비를 못 받으므로 살해 동기 모순"
        ]
    },
    {
        "id": "clue_13",
        "num": "13",
        "title": "박서준 피해자 모임 비밀 메모",
        "zone": "김유은 스마트폰 [화장실 선반]",
        "tag": "SECRET DOSSIER",
        "tag_color": "#00ddaa",
        "icon": "📝",
        "details": [
            "• 서준에게 사기당한 대학생 피해자 모임 오픈채팅방",
            "• 유은은 피해자 가족으로서 장부 증거 수집차 잠입",
            "• 살인 목적이 아닌 사기 입증이 방문 목적임 입증"
        ]
    },
    {
        "id": "clue_14",
        "num": "14",
        "title": "바 카운터 기본 비치용 빨대통",
        "zone": "바 카운터 [디스펜서]",
        "tag": "DISPENSARY CHECK",
        "tag_color": "#ffaa00",
        "icon": "🥤",
        "details": [
            "• 파티룸 기본 비치용은 일반 갈색 종이 스트로우뿐",
            "• '블랙 해골 모양 플라스틱 빨대'는 공용 비치품 아님",
            "• 서준의 빨대는 외부에서 개별 지참된 것임 증명"
        ]
    }
]

W, H = 800, 500
for c in clues_data:
    img = Image.new("RGBA", (W, H), "#0b1220")
    draw = ImageDraw.Draw(img)

    # Grid background
    for x in range(0, W, 20):
        draw.line([(x, 0), (x, H)], fill="#101c30", width=1)
    for y in range(0, H, 20):
        draw.line([(0, y), (W, y)], fill="#101c30", width=1)

    # Outer border
    draw.rectangle([(12, 12), (W - 12, H - 12)], outline="#1e3a5f", width=2)
    draw.rectangle([(16, 16), (W - 16, H - 16)], outline="#0f223a", width=1)

    # Top header bar
    draw.rectangle([(18, 18), (W - 18, 70)], fill="#0f1f38", outline="#254b77", width=1)
    draw.rectangle([(25, 25), (105, 63)], fill=c["tag_color"], outline="#ffffff", width=1)
    draw.text((35, 30), f"#{c['num']}", fill="#ffffff", font=font_title)

    draw.text((120, 26), f"EVIDENCE ITEM #{c['num']}", fill="#00d4ff", font=font_code)
    draw.text((120, 45), f"LOCATION: {c['zone']}", fill="#9fb3c8", font=font_meta)

    # Tag badge
    draw.rectangle([(W - 200, 28), (W - 25, 60)], fill="#081424", outline=c["tag_color"], width=1)
    draw.text((W - 185, 36), c["tag"], fill=c["tag_color"], font=font_code)

    # Left Icon box
    draw.rectangle([(30, 95), (180, 245)], fill="#081424", outline=c["tag_color"], width=2)
    draw.text((75, 135), c["icon"], fill="#ffffff", font=font_large_icon)
    draw.rectangle([(30, 215), (180, 245)], fill=c["tag_color"], outline=c["tag_color"], width=1)
    draw.text((45, 222), "FORENSIC CASE", fill="#ffffff", font=font_meta)

    # Right Content Box
    draw.rectangle([(200, 95), (W - 30, 430)], fill="#0a172c", outline="#1c3558", width=1)

    # Clue Title
    draw.text((220, 115), c["title"], fill="#ffffff", font=font_title)
    draw.line([(220, 155), (W - 50, 155)], fill="#204068", width=2)

    # Clue Details
    cur_y = 175
    for det in c["details"]:
        draw.text((225, cur_y), det, fill="#e1ecf7", font=font_sub)
        cur_y += 40

    # Bottom Footer Bar
    draw.rectangle([(18, 445), (W - 18, 482)], fill="#091424", outline="#193354", width=1)
    draw.text((30, 454), "POLICE DEPT CRIME SCENE INVESTIGATION DIVISION | LUNA HOUSE PENTHOUSE", fill="#5a7a9c", font=font_meta)
    draw.text((W - 180, 454), "STATUS: VERIFIED", fill="#00ffaa", font=font_meta)

    out_file = os.path.join(CLUES_DIR, f"{c['id']}.png")
    img.save(out_file, "PNG")

print("Generated all 14 evidence card images successfully!")
