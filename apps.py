from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'
    verbose_name = 'My App'

    def ready(self):
        import myapp.signals
