# Generated by Django 5.0.6 on 2024-06-21 00:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_comment_timeof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='verified',
        ),
        migrations.RemoveField(
            model_name='product',
            name='certified',
        ),
        migrations.AlterField(
            model_name='comment',
            name='timeof',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 0, 22, 32, 854067)),
        ),
    ]
