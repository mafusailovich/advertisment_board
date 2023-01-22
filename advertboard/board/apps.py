from django.apps import AppConfig


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

    #подключаем сигналы из board
    def ready(self):
        import board.signals
