# Generated by Django 2.1.2 on 2018-11-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]