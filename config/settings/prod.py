from .base import *
import os

ALLOWED_HOSTS = ['52.78.122.148', 'ainf.shop']
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']
DEBUG = False
