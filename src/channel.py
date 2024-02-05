from googleapiclient.discovery import build
import json
from pprint import pprint
import os


class Channel:
    # Класс для ютуб-канала
    api_key: str = os.getenv('YT_API_KEY')
    __channel: dict = None
    # Специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.video_count = self.get_info()['items'][0]['statistics']['videoCount']
        self.description: str = self.get_info()['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriber_count: int = self.get_info()['items'][0]['statistics']['subscriberCount']
        self.name: int = self.get_info()['items'][0]['snippet']['title']
        self.view_count: int = self.get_info()['items'][0]['statistics']['viewCount']

    def get_info(self) -> dict:
        if self.__channel is None:
            self.__channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return self.__channel

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(self.__channel)

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    @classmethod
    def get_service(cls) -> str:
        return cls.youtube

    def to_json(self, json_file: str) -> None:
        """Записывает данные канала в указанный аргументом json file"""
        with open(json_file, 'w', encoding='utf8') as f:
            json.dump(self.__channel, f, indent=2, ensure_ascii=False)

    def __str__(self) -> str:
        """Выводит информацию для пользователя"""
        return f'{self.name} ({self.url})'

    def __add__(self, other) -> int:
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other) -> int:
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __sub__(self, other) -> int:
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other) -> int:
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other) -> bool:
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other) -> bool:
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other) -> bool:
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other) -> bool:
        return int(self.subscriber_count) == int(other.subscriber_count)

    def __repr__(self) -> str:
        """Выводит информацию для разработчика"""
        return f'{self.__channel_id, self.__channel, self.video_count, self.description, self.url, self.subscriber_count, self.name, self.view_count}'
