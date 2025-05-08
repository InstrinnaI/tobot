from telegram import Update
from telegram.ext import Application, ContextTypes
import logging

class TelegramNotifier:
    def __init__(self, token, channel_id):
        self.application = Application.builder().token(token).build()
        self.channel = channel_id

    async def send(self, video):
        text = (
            f"🔔 Новое видео (дата публикации: {video['published_at']}):\n"
            f"{video['link']}"
        )
        try:
            await self.application.bot.send_message(self.channel, text)
            logging.info(f"Sent video {video['id']}")
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
            raise
