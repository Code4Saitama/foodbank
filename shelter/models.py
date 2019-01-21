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
    
