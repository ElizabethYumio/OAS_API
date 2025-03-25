from django.db import models
from django.utils import timezone

class Tag(models.Model):
    id = models.AutoField(
        primary_key = True,
    )
    name = models.CharField(
        max_length = 50,
        unique = True
    )
    prime_color = models.CharField(
        max_length = 50,
        blank = True,
    )
    created_date = models.DateTimeField(
        null = True
    )
    updated_date = models.DateTimeField(
        null = True
    )
    related_tags = models.ManyToManyField(
        'self', 
        blank = True,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super(Tag, self).save(*args, **kwargs)
