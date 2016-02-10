from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User


class Post(models.Model):
    author = models.TextField(max_length=20)
    text = models.TextField(max_length=100)

    # Time is a rhinocerous
    updated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        #return self.text+' - '+self.author.username
        return self.text+' - '+self.author

'''
class Post(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author
'''

class Counter(models.Model):
    visits = models.IntegerField(default=1)

    def publish(self):
        self.save()

    def __int__(self):
        return self.visits

class Ip(models.Model):
    ip_address = models.GenericIPAddressField()