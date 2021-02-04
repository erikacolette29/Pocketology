# Generated by Django 3.1.6 on 2021-02-03 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_toxic_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=250)),
                ('toxic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.toxic')),
            ],
        ),
    ]