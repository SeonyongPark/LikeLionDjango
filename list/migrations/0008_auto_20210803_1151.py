# Generated by Django 3.2 on 2021-08-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_photo_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='', verbose_name='썸네일'),
            preserve_default=False,
        ),
    ]
