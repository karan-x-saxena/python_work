# Generated by Django 4.0.2 on 2022-05-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat','0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=50)),
            ],
        ),
    ]
