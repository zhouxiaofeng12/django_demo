# -*- coding: utf-8 -*-
"""
    数据库操作(person类)

        all函数--全部
        get函数--单个
        filter函数--过滤多个
        exclude函数--除此以外

        create--创建
        update--更新(仅用于多个)
        delete--删除(一个或多个)

"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
django.setup()


# QuerySet创建对象的方法
def people_person_create():
    from people.models import Person
    # 第一种
    print(Person.objects.create(name='Zhoufeng', age=23))
    print(Person.objects.create(name='Zhoufeng', age=24))
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


# 临时补充数据
def temp():
    from people.models import Person
    p = Person(name='wz', age=13)
    p.save()
    p = Person(name='wz', age=23)
    p.save()
    p = Person(name='wangshijie', age=23)
    p.save()


"""
    使用get时可能会报错,原因是存在符合条件的多个数据 不能使用get
        people.models.MultipleObjectsReturned: get() returned more than one Person -- it returned 2!
"""


# 查询方法
def people_person_query():
    from people.models import Person
    # 获取所有对象
    print(Person.objects.all())

    # 获取name条件对象 单个
    print(Person.objects.get(name='WZ'))

    # 获取name条件对象 多个
    print(Person.objects.filter(name='Zhoufeng'))

    # 获取name条件对象(不区分大小写)
    print(Person.objects.filter(name__iexact='wz'))

    # 获取name条件对象(包含"wz"的人)
    print(Person.objects.filter(name__icontains='wz'))

    # 使用正则筛选条件
    print(Person.objects.filter(name__regex='^wz'))
    print(Person.objects.filter(name__iregex='^wz'))  # 加i表示忽视大小写

    # 排除符合某条件的
    print(Person.objects.exclude(name__iregex='^wz'))
    print(Person.objects.filter(name__iregex='^wz').exclude(age=13))

    # 切片操作，获取前2个人
    print(Person.objects.all()[:2])


# 删除方法
def people_person_del():
    from people.models import Person
    # 删除某条数据 返回(该数据所在表中的位置, {所删数据})
    print(Person.objects.filter(name='wz').delete())
    # 删除所有 Person 记录
    print(Person.objects.all().delete())


# 更新方法
def people_person_update():
    from people.models import Person

    # 名称中包含"Zhoufeng"的都改成zhouxiaofeng (批量更新--filter)
    Person.objects.filter(name__contains="Zhoufeng").update(name='zhouxiaofeng')

    # 全数据更新--all
    Person.objects.all().update(age=666)

    # 单个更新(同新增)
    p = Person.objects.get(name='wangshijie')
    p.name = 'wsj'
    p.age = 777
    p.save()


if __name__ == '__main__':
    # people_person_create()
    # temp()
    people_person_del()
    # people_person_update()
    # people_person_query()
    print('Done...')
