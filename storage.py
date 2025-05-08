import sqlite3
from pathlib import Path

class Storage:
    def __init__(self, db_path='data/bot.db'):
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id TEXT PRIMARY KEY,
                published_at TEXT
            )
        ''')

    def is_seen(self, video_id):
        cur = self.conn.execute(
            'SELECT 1 FROM videos WHERE id = ?', (video_id,)
        )
        return cur.fetchone() is not None

    def mark_seen(self, video_id, published_at):
        self.conn.execute(
            'INSERT OR IGNORE INTO videos (id, published_at) VALUES (?, ?)',
            (video_id, published_at)
        )
        self.conn.commit()
