import urllib.request
import ssl
from html.parser import HTMLParser

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.images = []
    def handle_data(self, data):
        text = data.strip()
        if text and len(text) > 2 and "{" not in text and "}" not in text:
            self.text.append(text)
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src' and attr[1].startswith('http'):
                    self.images.append(attr[1])

urls = [
    "https://jingyisong.com",
    "https://jingyisong.com/biography/%E5%85%B3%E4%BA%8E%E6%88%91",
    "https://jingyisong.com/gallery/%E7%85%A7%E7%89%87",
    "https://jingyisong.com/contact-me/%E8%81%94%E7%B3%BB%E6%88%91",
    "https://jingyisong.com/review/%E7%95%99%E8%A8%80"
]

with open('content_scrape.txt', 'w') as f:
    for url in urls:
        f.write(f"\n\n=== {url} ===\n")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, context=ctx) as response:
                html = response.read().decode('utf-8')
                parser = MyHTMLParser()
                parser.feed(html)
                f.write("TEXT:\n")
                for t in set(parser.text):
                    f.write(t + "\n")
                f.write("IMAGES:\n")
                for img in set(parser.images):
                    f.write(img + "\n")
        except Exception as e:
            f.write(f"Error: {e}\n")
