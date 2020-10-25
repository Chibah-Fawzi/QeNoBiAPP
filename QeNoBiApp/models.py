from django.db import models

# Create your models here.


class Group(models.Model):
    user = models.CharField(max_length=30, default="test")
    item = models.CharField(max_length=40, default="test")
    period = models.CharField(max_length=30, default="test")
    depth = models.CharField(max_length=30, default="test")
    support = models.CharField(max_length=30, default="test")


class Link(models.Model):
    group_source = models.CharField(max_length=30, default="test")
    group_target = models.CharField(max_length=30, default="test")
    user = models.CharField(max_length=30, default="test")
