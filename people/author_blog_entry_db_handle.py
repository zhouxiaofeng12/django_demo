# -*- coding: utf-8 -*-
"""
    数据库操作(Blog类\Author类\Entry类)
        exists函数--是否存在
        count函数--数据的数量

"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
django.setup()


def people_blog_create():
    from people.models import Blog
    if not Blog.objects.exists():
        print('没有Entry数据')

    b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    b.save()

    print('当前Entry数量为:' + str(Blog.objects.count()))


def people_author_create():
    from people.models import Author
    Author.objects.create(name='WeizhongTu', email='tuweizhong@163.com')
    Author.objects.create(name='WeizhongTu', email='tuweizhong@163.com')
    twz = Author(name='tu', email='222@163.com')
    twz.save()
    twz1 = Author(name='zhou', email='444@163.com')
    twz1.save()
    twz2 = Author(name='wang', email='777@163.com')
    twz2.save()


# 查询方法
def people_author_query():
    from people.models import Author
    print(Author.objects.all().filter(name='WeizhongTu')
          .filter(email='666@163.com'))

    print(Author.objects.all().order_by('name'))  # 按name升序
    print(Author.objects.all().order_by('-name'))  # 按name降序

    # 查询后两条数据
    # print(Author.objects.all()[:-2])  # 不支持负索引 Negative indexing is not supported
    print(Author.objects.reverse()[:2])


# 删除方法
def people_del():
    from people.models import Blog
    from people.models import Author
    Blog.objects.all().delete()
    Author.objects.all().delete()


if __name__ == '__main__':
    # people_del()
    # people_blog_create()
    # people_author_create()
    people_author_query()

    print('Done...')
