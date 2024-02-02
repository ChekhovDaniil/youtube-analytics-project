from googleapiclient.discovery import build
import json
from pprint import pprint
import os

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.__channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(self.__channel)

    @property
    def channel_id(self) -> None:
        raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    @property
    def channel_name(self) -> str:
        """Возвращает название канала"""
        name: str = self.__channel['items'][0]['statistics']['videoCount']
        return name

    @property
    def channel_description(self) -> str:
        """Возвращает описание канала"""
        description: str = self.__channel['items'][0]['snippet']['description']
        return description

    @property
    def channel_url(self):
        """Возвращает ссылку канала"""
        url = "https://www.youtube.com/channel/" + self.__channel_id
        return url

    @property
    def channel_subscriber_count(self) -> int:
        """Возвращает количество подписчиков канала"""
        subscriber_count: int = self.__channel['items'][0]['statistics']['subscriberCount']
        return subscriber_count

    @property
    def channel_video_count(self) -> int:
        """Возвращает количество видео канала"""
        video_count: int = self.__channel['items'][0]['snippet']['title']
        return video_count

    @property
    def channel_view_count(self) -> int:
        """Возвращает количество просмотров канала"""
        view_count: int = self.__channel['items'][0]['statistics']['viewCount']
        return view_count

    @classmethod
    def get_service(cls) -> str:
        return cls.youtube

    def to_json(self, json_file: str) -> None:
        """Записывает данные канала в указанный аргументом json file"""
        with open(json_file, 'w', encoding='utf8') as f:
            json.dump(self.__channel, f, indent=2, ensure_ascii=False)
