# Generated by Django 3.1.6 on 2021-02-08 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_rating_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
    ]
