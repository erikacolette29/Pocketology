# Generated by Django 3.1.6 on 2021-02-06 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_herbphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toxic',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='toxic',
            name='funfact',
            field=models.CharField(max_length=100),
        ),
    ]
