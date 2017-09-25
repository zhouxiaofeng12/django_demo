# -*- coding: utf-8 -*-
"""
    数据库操作
"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
django.setup()


# 新建一个对象
def people_person_create():
    from people.models import Person
    # 第一种
    print(Person.objects.create(name='Zhoufeng', age=25))

    # 第二种
    p = Person(name='WZ', age=13)
    p.save()

    # 第三种
    p = Person(name='TWZ')
    p.age = 23
    p.save()

    """
      第四种(防止重复 返回一个元组，第一个为Person对象 第二个为True或False 即已经存在时返回False)
            (<Person: lalala>, True)
    """
    print(Person.objects.get_or_create(name='lalala', age=23))


def temp():
    from people.models import Person
    p = Person(name='wz', age=13)
    p.save()
    p = Person(name='wangshijie', age=23)
    p.save()


def people_person_get():
    from people.models import Person
    # 获取所有对象
    print(Person.objects.all())

    # 获取name条件对象 单个
    print(Person.objects.get(name='WZ'))

    # 获取name条件对象 多个
    print(Person.objects.filter(name='Zhoufeng'))

    # 获取name条件对象(不区分大小写)
    print(Person.objects.filter(name__iexact='wz'))

    # 切片操作，获取前2个人
    print(Person.objects.all()[:2])


if __name__ == '__main__':
    # people_person_create()
    # temp()
    people_person_get()
    print('Done...')
