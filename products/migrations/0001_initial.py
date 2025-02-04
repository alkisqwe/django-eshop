# Generated by Django 5.0.6 on 2024-06-13 03:34

import datetime
import django.db.models.deletion
import products.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=5000)),
                ('specifications', models.CharField(blank=True, default='', max_length=5000)),
                ('deliverytime', models.CharField(choices=[('1-3 Days', '1-3 Days'), ('1 Week', '1 Week'), ('15 Days', '15 Days'), ('1 Month', '1 Month')], default='1-3 Days', max_length=100)),
                ('certified', models.IntegerField()),
                ('price', models.FloatField()),
                ('categorys', models.CharField(choices=[('All Categories', 'All Categories'), ('Art', 'Art'), ('Baby', 'Baby'), ('Books', 'Books'), ('Business & Industrial', 'Business & Industrial'), ('Cameras & Photo', 'Cameras & Photo'), ('Cell Phones & Accessories', 'Cell Phones & Accessories'), ('Clothing, Shoes & Accessories', 'Clothing, Shoes & Accessories'), ('Computers/Tablets & Networking', 'Computers/Tablets & Networking'), ('Consumer Electronics', 'Consumer Electronics'), ('Crafts', 'Crafts'), ('Dolls & Bears', 'Dolls & Bears'), ('DVDs & Movies', 'DVDs & Movies'), ('Gift Cards & Coupons', 'Gift Cards & Coupons'), ('Health & Beauty', 'Health & Beauty'), ('Home & Garden', 'Home & Garden'), ('Jewelry & Watches', 'Jewelry & Watches'), ('Music', 'Music'), ('Musical Instruments & Gear', 'Musical Instruments & Gear'), ('Pet Supplies', 'Pet Supplies'), ('Pottery & Glass', 'Pottery & Glass'), ('Real Estate', 'Real Estate'), ('Specialty Services', 'Specialty Services'), ('Sporting Goods', 'Sporting Goods'), ('Sports Mem, Cards & Fan Shop', 'Sports Mem, Cards & Fan Shop'), ('Tickets & Experiences', 'Tickets & Experiences'), ('Toys & Hobbies', 'Toys & Hobbies'), ('Travel', 'Travel'), ('Video Games & Consoles', 'Video Games & Consoles'), ('Everything Else', 'Everything Else')], default='Everything Else', max_length=100)),
                ('image1', models.ImageField(upload_to=products.models.productimages_path)),
                ('image2', models.ImageField(upload_to=products.models.productimages_path)),
                ('image3', models.ImageField(upload_to=products.models.productimages_path)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('verified', models.IntegerField(default=0)),
                ('helpfull', models.IntegerField(default=0)),
                ('stars', models.IntegerField()),
                ('timeof', models.DateTimeField(default=datetime.datetime(2024, 6, 13, 3, 34, 14, 481537))),
                ('image1', models.ImageField(upload_to=products.models.productimages_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
