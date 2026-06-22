import http.server
import os
import sys

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def route_path(self):
        # Normalize double slashes and strip trailing slashes
        clean_path = self.path.split('?')[0].split('#')[0]
        if clean_path.endswith('/') and len(clean_path) > 1:
            clean_path = clean_path.rstrip('/')

        # 1. Check if the exact requested path exists as a file (e.g., style.css, script.js, images/hero.jpg)
        translated = self.translate_path(self.path)
        if os.path.exists(translated) and not os.path.isdir(translated):
            return

        # 2. Map root '/' to index.html
        if clean_path == '/':
            self.path = '/index.html'
            return

        # 3. Map extensionless URLs (e.g., /biography -> biography.html)
        html_path = clean_path + '.html'
        translated_html = self.translate_path(html_path)
        if os.path.exists(translated_html):
            # Preserve query parameters/anchors if any
            suffix = self.path[len(clean_path):]
            self.path = html_path + suffix
            return

        # 4. Serve 404.html if it exists (for unrecognized routing)
        translated_404 = self.translate_path('/404.html')
        if os.path.exists(translated_404):
            self.path = '/404.html'
            return

    def do_GET(self):
        self.route_path()
        super().do_GET()

    def do_HEAD(self):
        self.route_path()
        super().do_HEAD()

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
