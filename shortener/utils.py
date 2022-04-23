"""shortener utils
"""
from django.utils.crypto import get_random_string
from .models import Url


def generate_uuid() -> str:
    while True:
        uuid = get_random_string(8)
        other_uuid = Url.objects.filter(uuid=uuid)
        if not other_uuid.exists():
            return uuid
