# Generated by Django 4.1 on 2022-09-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
