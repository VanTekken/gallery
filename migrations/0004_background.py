# Generated by Django 2.1.2 on 2018-11-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_fileupload_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_name', models.CharField(max_length=200)),
                ('template_url', models.CharField(max_length=200)),
            ],
        ),
    ]