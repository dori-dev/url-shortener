from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=2048)
    uuid = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.link[:32]
