"""
    数据库接口相关的接口（QuerySet API)
        从数据库中查询出来的结果一般是一个集合，这个集合叫做QuerySet

    此类作为数据库的对象类
        简单的理解: 继承自models.Model的类 Django自动生成对应的数据库表
            每写一个类
                调用python manage.py makemigrations # 创建migrations用于将models中的类映射成表
                再调用python manage.py migrate # 同步数据库
                相应的会在migrations文件夹中生成建表语句


"""
from django.db import models


# 新建了一个Person类，继承自models.Model
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    """
        2.7使用def __unicode__(self)
        3.0以上使用def __str__(self)  类似于java的toString方法
    """

    def __str__(self):
        return self.name + str(self.age)


# Blog类，继承自models.Model
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


# Author类，继承自models.Model
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)+str(self.email)


# Entry类，继承自models.Model
class Entry(models.Model):
    blog = models.ForeignKey(Blog)  # 外键 用于关联Blog对象
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)  # 多对多Author对象
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
