import uuid

from django.db import models
from django.db.models.fields import CharField, TextField

class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        null=False,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def last_messages():
        return Message.objects.order_by('-created_at').all()[:10]

    def __str__(self):
        return f"{self.username}: {self.text}"