# Generated by Django 5.1.7 on 2025-03-12 08:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomBlog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='panier',
            unique_together={('user',)},
        ),
    ]
