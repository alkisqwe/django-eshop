# Generated by Django 5.0.6 on 2024-06-19 23:13

import datetime
import products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_comment_timeof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.productimages_path),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timeof',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 23, 13, 50, 211758)),
        ),
    ]
