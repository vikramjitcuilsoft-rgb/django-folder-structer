from django.apps import AppConfig

class ConfigApp(AppConfig):
    name = "config"

    def ready(self):
        from common.db_logger import log_database_info
        log_database_info()
