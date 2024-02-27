from googleapiclient.discovery import build
import os


class Connection:
    """Класс-миксин для получения api-ключа и подключения к сервису"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_service(cls) -> str:
        return cls.youtube
