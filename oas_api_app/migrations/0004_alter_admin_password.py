# Generated by Django 5.0.10 on 2025-01-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oas_api_app', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
