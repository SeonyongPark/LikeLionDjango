# Generated by Django 3.2 on 2021-08-04 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0008_whodonate_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('body', models.CharField(max_length=500)),
                ('thumbnail', models.ImageField(upload_to='thumbnail/', verbose_name='썸네일')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='userinfo/', verbose_name='사진')),
                ('description', models.TextField()),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_info.post1')),
            ],
        ),
    ]
