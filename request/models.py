from django.db import models

# Create your models here.
from django.contrib.gis.db import models
class Shelter(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    timestamp = models.CharField(max_length=24)
    begin = models.CharField(max_length=24)
    end = models.CharField(max_length=24)
    altitudemo = models.CharField(max_length=254)
    tessellate = models.IntegerField()
    extrude = models.IntegerField()
    visibility = models.IntegerField()
    draworder = models.IntegerField()
    icon = models.CharField(max_length=254)
    geom = models.PointField(srid=4326)
    class Meta:
        db_table = 'shelter'

class Timeline(models.Model):
    title = models.CharField(max_length=128)
    message = models.TextField()
    progress = models.FloatField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    #外部キー
    shelter = models.ForeignKey(Shelter,on_delete=models.CASCADE)

    class Meta:
        db_table = 'timeline'


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'

class Product(models.Model):
    maker = models.CharField(max_length=100)
    name = models.CharField(max_length= 255)
    jancode = models.CharField(max_length=100)
    text1 = models.TextField()
    text2 = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    # 外部キー
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

class Stock(models.Model):
    stock = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    #外部キー
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table = 'stock'

class Request(models.Model):
    quantity = models.IntegerField()
    message = models.TextField()
    unit = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    #外部キー
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    timeline = models.ForeignKey(Timeline,on_delete=models.CASCADE)

    class Meta:
        db_table = 'request'

class Answer(models.Model):
    quantity = models.IntegerField()
    message = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    #外部キー
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    request = models.ForeignKey(Request,on_delete=models.CASCADE)

    class Meta:
        db_table = 'answer'
