# Generated by Django 5.0.6 on 2024-06-19 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_comment_timeof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timeof',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 2, 13, 43, 280515)),
        ),
    ]
