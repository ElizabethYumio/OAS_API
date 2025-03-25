import uuid
from django.db import models
from django.utils import timezone

from .user import User
from .item import Item

class Bid(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    buyer = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True
    )
    item = models.ForeignKey(
        Item,
        related_name='bids',
        on_delete = models.SET_NULL,
        null = True
    )
    amount = models.DecimalField(
        max_digits = 19,
        decimal_places = 3
    )
    created_date = models.DateTimeField(
        null = True
    )
    updated_date = models.DateTimeField(
        null = True
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super(Bid, self).save(*args, **kwargs)
