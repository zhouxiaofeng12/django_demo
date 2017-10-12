# -*- coding: utf-8 -*-
"""
    数据迁移操作 [不指定appname时默认为导出所有的app]
        python manage.py dumpdata [appname] > [json文件]
        栗子:
            # 导出Model(people)数据
            python manage.py dumpdata people > people_data.json

            # 导入Model(people)数据
            python manage.py loaddata people_data.json



"""
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()

if __name__ == '__main__':

    print('Done...')
