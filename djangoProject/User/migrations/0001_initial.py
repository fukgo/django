# Generated by Django 5.0 on 2024-01-05 05:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='user/avatars/default.jpg', null=True, upload_to='user/avatars/%Y%m%d/')),
                ('introduction', models.TextField(blank=True, default='无', max_length=120, null=True)),
                ('gender', models.SmallIntegerField(blank=True, choices=[(0, '女'), (1, '男')], default=1, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]