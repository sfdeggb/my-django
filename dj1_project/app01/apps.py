from django.apps import AppConfig
#负责启动app 

class App01Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app01'
