# Generated by Django 5.0.6 on 2024-06-29 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0054_alter_comment_timeof_delete_cartmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timeof',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 29, 15, 29, 56, 118126)),
        ),
    ]
