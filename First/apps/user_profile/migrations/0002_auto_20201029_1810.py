# Generated by Django 3.1.2 on 2020-10-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board_required',
            name='identity',
            field=models.CharField(default='Change it', max_length=100),
        ),
        migrations.AddField(
            model_name='button_required',
            name='identity',
            field=models.CharField(default='Change it', max_length=100),
        ),
    ]
