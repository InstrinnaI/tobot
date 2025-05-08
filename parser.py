import requests
from bs4 import BeautifulSoup
from datetime import datetime

class VideoParser:
    def __init__(self, site_url):
        self.url = site_url

    def fetch_latest(self):
        resp = requests.get(self.url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Замените .video-item и .date на селекторы вашего сайта
        items = soup.select('.video-item')
        videos = []
        for item in items:
            link = item.find('a')['href']
            published_text = item.select_one('.date').text.strip()
            pub_dt = datetime.strptime(published_text, '%Y-%m-%d')
            vid_id = link.split('/')[-1]
            videos.append({
                'id': vid_id,
                'link': link,
                'published_at': pub_dt.isoformat()
            })
        return videos
