from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class AppModel(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title
