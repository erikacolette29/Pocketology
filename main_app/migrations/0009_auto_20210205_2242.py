# Generated by Django 3.1.6 on 2021-02-05 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210205_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='herb',
            old_name='addon',
            new_name='addons',
        ),
    ]
