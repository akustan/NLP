# Generated by Django 3.0.2 on 2020-03-12 00:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_addrss_feed_added'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddRSS',
            new_name='RSS',
        ),
    ]
