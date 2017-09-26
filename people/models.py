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


# Entry类，继承自models.Model
class Entry(models.Model):
    blog = models.ForeignKey(Blog)  # 外键 用于关联Blog对象
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


"""
    一篇文章只有一个作者(Author)，
    一个作者可以有多篇文章(Article)，
    一篇文章可以有多个标签（Tag)
"""


# Author作者类，继承自models.Model
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return str(self.name) + " / " + str(self.email)


# Article文章类，继承自models.Model
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)  # 多对一
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')  # 多对多

    def __str__(self):
        return str(self.title) + " / " + str(self.author)


# Tag标签类，继承自models.Model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
