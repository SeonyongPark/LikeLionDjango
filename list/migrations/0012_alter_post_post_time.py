# Generated by Django 3.2 on 2021-08-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0011_alter_post_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
