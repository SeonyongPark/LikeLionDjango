# Generated by Django 3.2 on 2021-08-05 03:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0013_alter_post1_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whodonate',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
