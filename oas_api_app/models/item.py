import uuid
from django.db import models
from django.utils import timezone

from .user import User
from .tag import Tag

class Item(models.Model):
    class ItemStatus(models.IntegerChoices):
        NEW = 0
        ACTIVE = 1
        DONE = 2
        INACTIVE = 3

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    name = models.CharField(
        max_length = 50
    )
    image_url = models.CharField(
        max_length = 1024,
        blank = True
    )
    description = models.TextField(
        blank = True
    )
    start_price = models.DecimalField(
        max_digits = 19,
        decimal_places = 3
    )
    step = models.DecimalField(
        max_digits = 19,
        decimal_places = 3
    )
    end_date = models.DateField(
        blank = True
    )
    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True
    )
    status = models.IntegerField(
        choices = ItemStatus,
        null = True
    )
    created_date = models.DateTimeField(
        null = True
    )
    updated_date = models.DateTimeField(
        null = True
    )
    tags = models.ManyToManyField(
        Tag, 
        blank = True,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super(Item, self).save(*args, **kwargs)
