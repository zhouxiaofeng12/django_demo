# -*- coding: utf-8 -*-
"""
    数据库操作(Blog类\Author类\Entry类)

"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
django.setup()


def people_blog_create():
    from people.models import Blog
    b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    b.save()


def people_author_create():
    from people.models import Author
    Author.objects.create(name="WeizhongTu", email="tuweizhong@163.com")
    twz = Author(name="WeizhongTu", email="tuweizhong@163.com")
    twz.save()


def people_entry_create():
    from people.models import Entry
    b = Entry(name='Beatles Blog', tagline='All the latest Beatles news.')
    b.save()


# 查询方法
def people_person_query():
    from people.models import Entry
    entry = Entry.objects.get(pk=1)
    from people.models import Blog
    cheese_blog = Blog.objects.get(name="Cheddar Talk")
    entry.blog = cheese_blog
    entry.save()


# 删除方法
def people_person_del():
    from people.models import Person
    # 删除某条数据 返回(该数据所在表中的位置, {所删数据})
    print(Person.objects.filter(name='wz').delete())
    # 删除所有 Person 记录
    print(Person.objects.all().delete())


if __name__ == '__main__':
    people_entry_create()
    print('Done...')
