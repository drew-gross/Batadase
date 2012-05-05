from django.db import models

class Key(models.Model):
    key = models.CharField(max_length=500)

class Value(models.Model):
    key = models.ForeignKey(Key)
    value = models.CharField(max_length=10000)