from telegram import Bot
import logging

class TelegramNotifier:
    def __init__(self, token, channel_id):
        # передаём оба параметра напрямую
        self.bot = Bot(token=token)
        self.channel = channel_id

    def send(self, video):
        text = (
            f"🔔 Новое видео (дата публикации: {video['published_at']}):\n"
            f"{video['link']}"
        )
        try:
            self.bot.send_message(self.channel, text)
            logging.info(f"Sent video {video['id']}")
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
            raise
