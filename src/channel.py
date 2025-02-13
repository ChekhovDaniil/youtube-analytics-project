import json
from pprint import pprint
from src.mixins import Connection


class Channel(Connection):
    # Класс для ютуб-канала
    __channel: dict = None

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        data = self.get_info()['items'][0]
        self.video_count = data['statistics']['videoCount']
        self.description: str = data['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriber_count: int = data['statistics']['subscriberCount']
        self.name: int = data['snippet']['title']
        self.view_count: int = data['statistics']['viewCount']

    def get_info(self) -> dict:
        """Если информации в словаре нет, возвращает информацию о канале."""
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
