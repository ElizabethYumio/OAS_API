# Generated by Django 5.0.10 on 2024-12-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oas_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='payment_info',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
