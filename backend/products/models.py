from django.db import models

from django.conf import settings

from django.db.models import Q

from datetime import datetime

import random

User = settings.AUTH_USER_MODEL # auth.user

TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            # show distinct results
            qs = (qs | qs2).distinct()
        return qs

# filter the query set based on it's public or not
class ProductManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self,query, user=None):
        return self.get_queryset().filter(public=True).search(query, user=user)


# Create your models here.
class Product(models.Model):

    user = models.ForeignKey(User, null=True, default=1, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    # search only public records 
    public = models.BooleanField(default=True)
    # publishing time
    publish_timestamp = models.DateTimeField(default=datetime.now())

    objects = ProductManager()


    def is_public(self) -> bool: # returns bool
        return self.public # True or False

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "%.2f" %(float(self.price) - float(self.price) * 0.8)