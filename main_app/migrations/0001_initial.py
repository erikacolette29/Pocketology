# Generated by Django 3.1.6 on 2021-02-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toxic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('funfact', models.TextField(max_length=250)),
                ('howtoxic', models.CharField(choices=[('Baby Strength', 'Baby Strength'), ('Oh Boy', 'Oh Boy'), ('Deadly', 'Deadly')], default='Baby Strength', max_length=15)),
            ],
        ),
    ]
