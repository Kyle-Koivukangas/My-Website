from django.apps import AppConfig


class myWebsiteAppConfig(AppConfig):
    name = 'myWebsite'

    def ready(self):
        from myWebsite import signals
