import uuid
from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    username = models.CharField(
        max_length = 30
    )
    email = models.EmailField(
        null = True
    )
    password = models.CharField(
        max_length = 100
    )
    address = models.CharField(
        max_length = 100,
        blank = True
    )
    phone = models.CharField(
        max_length = 100,
        blank = True
    )
    avatar_url = models.CharField(
        max_length = 1024,
        blank = True
    )
    created_date = models.DateTimeField(
        null = True
    )
    updated_date = models.DateTimeField(
        null = True
    )
    payment_info = models.CharField(
        max_length = 100,
        blank = True
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super(User, self).save(*args, **kwargs)


