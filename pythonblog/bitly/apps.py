# bitly라는 application이 누구를 부르고 어떤 작업을 할지에 대해서 따로 설정해줄 수 있다.
from django.apps import AppConfig


class BitlyAppConfig(AppConfig):
    name = "bitly"  # 앱이름

    # application이 실행될때 실행되는 함수
    def ready(self):
        from bitly.signals.post_save import post_save_bitlink
