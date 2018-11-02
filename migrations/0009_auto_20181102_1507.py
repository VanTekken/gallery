# Generated by Django 2.1.2 on 2018-11-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20181102_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('filename', models.FileField(upload_to='media/')),
                ('date_added', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nme', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('sld', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='backgrounds',
            name='backgroundselection_ptr',
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
        migrations.DeleteModel(
            name='Backgrounds',
        ),
        migrations.DeleteModel(
            name='BackgroundSelection',
        ),
    ]