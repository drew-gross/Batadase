from django.db import models

class Key(models.Model):
    key = models.CharField(max_length=500)

class Value(models.Model):
    models.ForeignKey(Key)
    models.CharField(max_length=10000)