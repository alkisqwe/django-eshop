# Generated by Django 5.0.6 on 2024-06-28 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_alter_comment_timeof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timeof',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 4, 3, 44, 502009)),
        ),
    ]
