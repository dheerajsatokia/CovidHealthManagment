# Generated by Django 3.2 on 2021-04-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_others'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='medical_support',
            field=models.BooleanField(default=False),
        ),
    ]