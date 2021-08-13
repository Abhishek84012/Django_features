'''Set AppConfig.
'''
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    '''Authentication config
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
