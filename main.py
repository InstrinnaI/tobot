import logging
import asyncio
from parser import VideoParser
from storage import Storage
from notifier import TelegramNotifier

# —————————————————————————————————————————————
#  Здесь указываете свои параметры:
SITE_URL     = "https://rt.pornhub.com/"      # <- Замените на URL сайта
TELEGRAM_TOKEN = "7579732690:AAEqXFb6s_jLBw8DEKzeUe1cMaeOF3IlAbM"  # <- Ваш токен из BotFather
CHANNEL_ID     = "@https://t.me/pornhubtyyt"              # <- Ваш канал, начиная с @
DB_PATH        = "data/bot.db"                   # <- Оставьте как есть или измените путь
# —————————————————————————————————————————————

async def check_for_new_videos():
    parser = VideoParser(SITE_URL)
    store  = Storage(DB_PATH)
    notifier = TelegramNotifier(TELEGRAM_TOKEN, CHANNEL_ID)

    videos = parser.fetch_latest()
    for vid in videos:
        if not store.is_seen(vid['id']):
            await notifier.send(vid)
            store.mark_seen(vid['id'], vid['published_at'])

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    asyncio.run(check_for_new_videos())
