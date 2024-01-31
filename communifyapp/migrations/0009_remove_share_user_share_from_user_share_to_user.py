# Generated by Django 5.0.1 on 2024-01-28 20:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communifyapp', '0008_rename_from_user_share_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='user',
        ),
        migrations.AddField(
            model_name='share',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share',
            name='to_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]