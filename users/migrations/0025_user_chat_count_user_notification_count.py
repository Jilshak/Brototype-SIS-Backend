# Generated by Django 4.2.4 on 2023-09-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_weekdetails_miscellenous_tasks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='notification_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]