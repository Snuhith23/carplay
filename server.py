import http.server
import socket
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    local_ip = get_ip()
    print("=" * 60)
    print("   MOTORCYCLE CARPLAY DASHBOARD SERVER")
    print("=" * 60)
    print(f"Local test URL:  http://localhost:{PORT}")
    print(f"iPhone WiFi URL: http://{local_ip}:{PORT}")
    print("=" * 60)
    print("IMPORTANT FOR IPHONE SAFARI GPS:")
    print("iOS Safari requires HTTPS for live GPS tracking.")
    print("For live motorcycle riding, deploy this folder to GitHub Pages (free HTTPS)")
    print("or an HTTPS tunnel (like Cloudflare Tunnel / ngrok).")
    print("=" * 60)
    print("Press Ctrl+C to stop the server.")
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
