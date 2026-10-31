#!/usr/bin/env python3
"""
할로윈 머더 미스터리 게임 로컬 실행기 & 실시간 투표 동기화 서버 (server.py)
같은 와이파이에 연결된 친구들이 스마트폰으로 접속하여 실시간으로
투표 진행 현황(1/9 ~ 9/9)을 공유하고 자동으로 다음 단계로 넘어갈 수 있도록 지원합니다.
"""

import http.server
import socket
import socketserver
import os
import sys
import json
import time

PORT = 8080
RUNTIME_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runtime_votes.json")

# In-memory Server State
SERVER_STATE = {
    "midtermVotes": {},
    "finalVotes": {},
    "updatedAt": int(time.time() * 1000)
}

def load_runtime_state():
    global SERVER_STATE
    if os.path.exists(RUNTIME_FILE):
        try:
            with open(RUNTIME_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    SERVER_STATE["midtermVotes"] = data.get("midtermVotes", {})
                    SERVER_STATE["finalVotes"] = data.get("finalVotes", {})
                    SERVER_STATE["updatedAt"] = data.get("updatedAt", int(time.time() * 1000))
                    print(f"📦 기존 투표 데이터 복원 완료 (중간 {len(SERVER_STATE['midtermVotes'])}명 / 최종 {len(SERVER_STATE['finalVotes'])}명)")
        except Exception as e:
            print(f"⚠️ 런타임 투표 파일 로드 실패 (초기화 진행): {e}")

def save_runtime_state():
    try:
        with open(RUNTIME_FILE, "w", encoding="utf-8") as f:
            json.dump(SERVER_STATE, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️ 투표 데이터 파일 저장 실패: {e}")

class MysteryServerHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for all local requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        clean_path = self.path.split('?')[0]
        if clean_path in ('/api/state', '/api/votes'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            self.end_headers()
            self.wfile.write(json.dumps(SERVER_STATE, ensure_ascii=False).encode('utf-8'))
            return
        
        # Fall back to static files (index.html, scenario.json, etc.)
        super().do_GET()

    def do_POST(self):
        clean_path = self.path.split('?')[0]
        
        if clean_path == '/api/vote':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                data = json.loads(body)

                vote_type = data.get('type')  # 'midterm' or 'final'
                voter_id = data.get('voterId')
                target_id = data.get('targetId')

                if vote_type == 'midterm' and voter_id and target_id:
                    SERVER_STATE['midtermVotes'][voter_id] = target_id
                    SERVER_STATE['updatedAt'] = int(time.time() * 1000)
                    save_runtime_state()
                    total_mid = len(SERVER_STATE['midtermVotes'])
                    print(f"🗳️ [1차 중간투표 접수] {voter_id} ➔ {target_id} (현재 {total_mid}/9명 완료)")

                elif vote_type == 'final' and voter_id and target_id:
                    SERVER_STATE['finalVotes'][voter_id] = target_id
                    SERVER_STATE['updatedAt'] = int(time.time() * 1000)
                    save_runtime_state()
                    total_fin = len(SERVER_STATE['finalVotes'])
                    print(f"⚖️ [최종 지목투표 접수] {voter_id} ➔ {target_id} (현재 {total_fin}/9명 완료)")

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'state': SERVER_STATE}, ensure_ascii=False).encode('utf-8'))
                return

            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
                return

        elif clean_path == '/api/reset':
            SERVER_STATE['midtermVotes'] = {}
            SERVER_STATE['finalVotes'] = {}
            SERVER_STATE['updatedAt'] = int(time.time() * 1000)
            save_runtime_state()
            print("🔄 [호스트] 전체 투표 데이터가 리셋되었습니다.")

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'state': SERVER_STATE}, ensure_ascii=False).encode('utf-8'))
            return

        super().do_POST()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def print_ascii_qr(url):
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        qr.make(fit=True)
        qr.print_ascii(invert=True)
    except ImportError:
        print("\n[TIP] 터미널에 스캔 가능한 QR 코드를 띄우려면: pip install qrcode")

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    load_runtime_state()

    local_ip = get_local_ip()
    url = f"http://{local_ip}:{PORT}"
    localhost_url = f"http://localhost:{PORT}"

    print("=" * 64)
    print("🎃 [할로윈 파티룸: 붉은 호박의 밤] 실시간 투표 동기화 웹서버 시작")
    print("=" * 64)
    print(f"\n📱 [친구들 스마트폰 접속 주소 (같은 Wi-Fi 연결 필요)]:")
    print(f"👉 \033[1;32m{url}\033[0m")
    print(f"\n💻 [노트북/호스트 접속 주소]:")
    print(f"👉 {localhost_url}\n")
    print("✨ 실시간 투표 동기화 API 활성화 (/api/state, /api/vote)")

    print_ascii_qr(url)

    print("\n" + "=" * 64)
    print("서버가 실행 중입니다. 투표 현황이 아래에 실시간 출력됩니다.")
    print("서버를 종료하려면 Ctrl + C 를 누르세요.")
    print("=" * 64 + "\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), MysteryServerHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 안전하게 종료합니다. 즐거운 할로윈 되세요! 🎃")

if __name__ == '__main__':
    main()
