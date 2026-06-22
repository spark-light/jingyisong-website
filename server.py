import http.server
import os
import sys

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Normalize double slashes and strip trailing slashes
        clean_path = self.path.split('?')[0].split('#')[0]
        if clean_path.endswith('/') and len(clean_path) > 1:
            clean_path = clean_path.rstrip('/')

        # 1. Check if the exact requested path exists as a file (e.g., style.css, script.js, images/hero.jpg)
        translated = self.translate_path(self.path)
        if os.path.exists(translated) and not os.path.isdir(translated):
            super().do_GET()
            return

        # 2. Map root '/' to index.html
        if clean_path == '/':
            self.path = '/index.html'
            super().do_GET()
            return

        # 3. Map extensionless URLs (e.g., /biography -> biography.html)
        html_path = clean_path + '.html'
        translated_html = self.translate_path(html_path)
        if os.path.exists(translated_html):
            # Preserve query parameters/anchors if any
            suffix = self.path[len(clean_path):]
            self.path = html_path + suffix
            super().do_GET()
            return

        # 4. Fallback to default handler
        super().do_GET()

if __name__ == '__main__':
    port = 8081
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, CleanURLHandler)
    print(f"Serving HTTP on port {port} with clean URLs (mapped pages)...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        sys.exit(0)
