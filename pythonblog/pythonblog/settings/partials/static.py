import os

from .base import PROJECT_ROOT_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

INTERNAL_IPS = [
    '127.0.0.1',
]

# Media Files
# join은 경로 합쳐주는 애라고 생각하면 된다.
MEDIA_ROOT = os.path.join(
    PROJECT_ROOT_DIR,
    "dist",
    "media",
)
MEDIA_URL = "/media/"
