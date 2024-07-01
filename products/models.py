from django.db import models
from django.conf import settings
import datetime

def productimages_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.owner.id, instance.pk, filename)

class Product(models.Model):
    CATEGORIES = [
        ('EE', 'Everything Else'),
        ('Art', 'Art'),
        ('Baby', 'Baby'),
        ('Books', 'Books'),
        ('BI', 'Business & Industrial'),
        ('CP', 'Cameras & Photo'),
        ('CPA', 'Cell Phones & Accessories'),
        ('CSA', 'Clothing, Shoes & Accessories'),
        ('CTN', 'Computers/Tablets & Networking'),
        ('CE', 'Consumer Electronics'),
        ('Crafts', 'Crafts'),
        ('DB', 'Dolls & Bears'),
        ('DM', 'DVDs & Movies'),
        ('GCC', 'Gift Cards & Coupons'),
        ('HB', 'Health & Beauty'),
        ('HG', 'Home & Garden'),
        ('JW', 'Jewelry & Watches'),
        ('Music', 'Music'),
        ('MIG', 'Musical Instruments & Gear'),
        ('PS', 'Pet Supplies'),
        ('PG', 'Pottery & Glass'),
        ('RE', 'Real Estate'),
        ('SS', 'Specialty Services'),
        ('SG', 'Sporting Goods'),
        ('SMCFS', 'Sports Mem, Cards & Fan Shop'),
        ('TE', 'Tickets & Experiences'),
        ('TH', 'Toys & Hobbies'),
        ('Travel', 'Travel'),
        ('VGC', 'Video Games & Consoles')
    ]
    DELIVERTIME = [
        ('1-3 Days', '1-3 Days'),
        ('1 Week', '1 Week'),
        ('15 Days', '15 Days'),
        ('1 Month', '1 Month')
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, blank=True, default="")
    specifications = models.CharField(max_length=5000, blank=True, default="")
    deliverytime = models.CharField(max_length=100, choices=DELIVERTIME, default='1-3 Days')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    price = models.FloatField()
    categorys = models.CharField(max_length=100, choices=CATEGORIES, default='Everything Else')
    image = models.ImageField(blank=True, null=True, upload_to=productimages_path)
    image2 = models.ImageField(blank=True, null=True, upload_to=productimages_path)
    image3 = models.ImageField(blank=True, null=True, upload_to=productimages_path)
    
    def save(self, *args, **kwargs):
        saved_image = self.image
        saved_image2 = self.image2
        saved_image3 = self.image3
        self.image = None
        self.image2 = None
        self.image3 = None
        super(Product, self).save(*args, **kwargs)
        self.image = saved_image
        self.image2 = saved_image2
        self.image3 = saved_image3
        if 'force_insert' in kwargs:
            kwargs.pop('force_insert')
        super(Product, self).save(*args, **kwargs)
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    stars = models.IntegerField()
    timeof = models.DateTimeField(default=datetime.datetime.now())
    image1 = models.ImageField(blank=True, null=True, upload_to=productimages_path)
    
    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image1 = self.image1
            self.image1 = None
            super(Comment, self).save(*args, **kwargs)
            self.image1 = saved_image1
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super(Comment, self).save(*args, **kwargs)

class Wishlist(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
