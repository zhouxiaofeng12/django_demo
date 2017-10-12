# -*- coding: utf-8 -*-
"""
    实例讲解--参考person_db_handle.py

"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


# QuerySet创建对象的方法
def people_person_create():
    from people.models import Person
    # 第一种
    # print(Person.objects.create(name='Zhoufeng', age=23))
    # print(Person.objects.create(name='Zhoufeng', age=24))
    # print(Person.objects.create(name='Zhoufeng', age=25))


# 查询方法
def people_person_query():
    from people.models import Person
    # 获取所有对象
    # print(Person.objects.all())


    # # 获取name条件对象 单个
    # print(Person.objects.get(name='WZ'))
    #
    # # 获取name条件对象 多个
    # print(Person.objects.filter(name='Zhoufeng'))
    #
    # # 获取name条件对象(不区分大小写)
    # print(Person.objects.filter(name__iexact='wz'))
    #
    # # 获取name条件对象(包含"wz"的人)
    # print(Person.objects.filter(name__icontains='wz'))
    #
    # # 使用正则筛选条件
    # print(Person.objects.filter(name__regex='^wz'))
    # print(Person.objects.filter(name__iregex='^wz'))  # 加i表示忽视大小写
    #
    # # 排除符合某条件的
    # print(Person.objects.exclude(name__iregex='^wz'))
    # print(Person.objects.filter(name__iregex='^wz').exclude(age=13))
    #
    # # 切片操作，获取前2个人
    # print(Person.objects.all()[:2])




if __name__ == '__main__':
    people_person_query()
    print('Done...')
