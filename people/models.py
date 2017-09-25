from django.db import models

"""
    与数据库相关的
    新建了一个Person类，继承自models.Model
"""


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    """
        2.7使用def __unicode__(self)
        3.0以上使用def __str__(self)  类似于java的toString方法
    """
    def __str__(self):
        return self.name
