from django.db import models
import datetime


class Counter(models.Model):
    visits = models.IntegerField(default=1)

    def publish(self):
        self.save()

    def __int__(self):
        return self.visits