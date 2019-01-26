# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Answer(models.Model):
    request = models.ForeignKey('Request', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Product(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING)
    maker = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    jancode = models.CharField(max_length=100, blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product'


class Progress(models.Model):
    shelter_id = models.IntegerField(blank=True, null=True)
    finish_rate = models.FloatField(blank=True, null=True)
    working_rate = models.FloatField(blank=True, null=True)
    waiting_rate = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'progress'


class Request(models.Model):
    timeline = models.ForeignKey('Timeline', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'request'


class Shelter(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)
    description = models.CharField(max_length=254, blank=True, null=True)
    timestamp = models.CharField(max_length=24, blank=True, null=True)
    begin = models.CharField(max_length=24, blank=True, null=True)
    end = models.CharField(max_length=24, blank=True, null=True)
    altitudemo = models.CharField(max_length=254, blank=True, null=True)
    tessellate = models.BigIntegerField(blank=True, null=True)
    extrude = models.BigIntegerField(blank=True, null=True)
    visibility = models.BigIntegerField(blank=True, null=True)
    draworder = models.BigIntegerField(blank=True, null=True)
    icon = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shelter'


class Stock(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    stock = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class Timeline(models.Model):
    title = models.CharField(max_length=128)
    message = models.TextField(blank=True, null=True)
    progress = models.FloatField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    shelter = models.ForeignKey(Shelter, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'timeline'
