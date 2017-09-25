from django.db import models

"""
    新建了一个Person类，继承自models.Model
"""


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
