# Generated by Django 5.0.10 on 2025-01-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oas_api_app', '0002_user_payment_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
