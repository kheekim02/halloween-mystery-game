#!/usr/bin/env python3
"""
할로윈 머더 미스터리 게임 로컬 실행기 (server.py)
같은 와이파이에 연결된 친구들이 스마트폰으로 즉시 접속할 수 있도록
로컬 IP 주소와 QR 코드를 터미널에 표시하고 웹 서버를 실행합니다.
"""

import http.server
import socket
import socketserver
import os
import sys

PORT = 8080

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def print_ascii_qr(url):
    try:
        # Try importing qrcode if available
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        qr.make(fit=True)
        qr.print_ascii(invert=True)
    except ImportError:
        # Fallback message
        print("\n[TIP] 'pip install qrcode'를 설치하시면 터미널에 스캔 가능한 QR 코드가 바로 표시됩니다.")

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    local_ip = get_local_ip()
    url = f"http://{local_ip}:{PORT}"
    localhost_url = f"http://localhost:{PORT}"

    print("=" * 60)
    print("🎃 [할로윈 파티룸: 붉은 호박의 밤] 모바일 웹서버 시작")
    print("=" * 60)
    print(f"\n📱 [친구들 스마트폰 접속 주소 (같은 Wi-Fi 필요)]:")
    print(f"👉 \033[1;32m{url}\033[0m")
    print(f"\n💻 [노트북/호스트 접속 주소]:")
    print(f"👉 {localhost_url}\n")

    print_ascii_qr(url)

    print("\n" + "=" * 60)
    print("서버가 실행 중입니다. 종료하려면 Ctrl + C 를 누르세요.")
    print("=" * 60 + "\n")

    Handler = http.server.SimpleHTTPRequestHandler
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다. 즐거운 할로윈 되세요! 🎃")

if __name__ == '__main__':
    main()
