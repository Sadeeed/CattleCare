from django.db import models


class CollarData(models.Model):
    topic = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic}"
