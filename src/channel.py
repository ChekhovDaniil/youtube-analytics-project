import os

from googleapiclient.discovery import build


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
        from pprint import pprint
        pprint(self.__channel)

    @property
    def channel_id(self):
        try:
            self.__channel_id
        except:
            raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    @property
    def channel_name(self):
        """Возвращает название канала"""
        name: str = self.__channel['items'][0]['statistics']['videoCount']
        return name

    @property
    def channel_description(self):
        """Возвращает описание канала"""
        description: str = self.__channel['items'][0]['snippet']['description']
        return description

    @property
    def channel_url(self):
        """Возвращает ссылку канала"""
        url = "https://www.youtube.com/channel/" + self.__channel_id
        return url

    @property
    def channel_subscriber_count(self):
        """Возвращает количество подписчиков канала"""
        subscriber_count: int = self.__channel['items'][0]['statistics']['subscriberCount']
        return subscriber_count

    @property
    def channel_video_count(self):
        """Возвращает количество видео канала"""
        video_count: int = self.__channel['items'][0]['snippet']['title']
        return video_count

    @property
    def channel_view_count(self):
        """Возвращает количество просмотров канала"""
        view_count: int = self.__channel['items'][0]['statistics']['viewCount']
        return view_count

    @classmethod
    def get_service(cls):
        return cls.youtube

    @staticmethod
    def to_json(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        import json
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
