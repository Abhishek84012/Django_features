from django.apps import AppConfig


class ECommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_commerce'

    def ready(self):
        pass
        #TODO Please uncomment whenever use signals. 
        # import e_commerce.signals
