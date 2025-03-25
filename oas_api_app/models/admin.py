from django.db import models
from django.utils import timezone

class Admin(models.Model):
    id = models.AutoField(
        primary_key = True,
        editable=False,
    )
    username = models.CharField(
        max_length = 30,
        unique = True
    )
    password = models.CharField(
        max_length = 100
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
        return super(Admin, self).save(*args, **kwargs)
