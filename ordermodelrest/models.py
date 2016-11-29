from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Merchandise(models.Model):
    name_merch = models.CharField(max_length=50)
    merch_price = models.CharField(max_length=100,blank=True,default='')
    merch_count = models.CharField(max_length=100)
    merch_enabled = models.BooleanField(default=1)
    merch_del = models.BooleanField(default=0)
    merch_description = models.TextField(blank=True, default='')

    class Meta:
        db_table = u'order_merch_cat'
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        return super(Merchandise, self).save(*args, **kwargs)

class MerchPhoto(models.Model):
    idmerch=models.ForeignKey(Merchandise)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True, max_length=255)