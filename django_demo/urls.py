# -*- coding: utf-8 -*-
"""
    总的urls配置文件
    定义视图函数相关的URL(网址)  （即规定 访问什么网址对应什么内容）
"""
from learn import views as learn_views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # http://127.0.0.1:8000/
    url(r'^$', learn_views.index),

    # http://127.0.0.1:8000/home
    url(r'^home/$', learn_views.home),

    # http://127.0.0.1:8000/add/?b=5
    url(r'^add/$', learn_views.add),

    # 这里的name对应页面的 {% url 'name' 参数 %} 中的name
    url(r'^query/(\d+)/$', learn_views.query, name='query'),

    # 重定向url到new_page/参数
    url(r'^whatever_url/(\d+)/$', learn_views.page_redirect, name='new_query'),
    url(r'^new_page/(\d+)/$', learn_views.new_query, name='new_page'),

    # http://127.0.0.1:8000/template
    url(r'^template/$', learn_views.template),

    # http://127.0.0.1:8000/form 使用form表单
    url(r'^form/$', learn_views.form),
    url(r'^add_form/$', learn_views.add_form),

    # http://127.0.0.1:8000/admin/
    url(r'^admin/', admin.site.urls),


    # http://127.0.0.1:8000/test
    url(r'^test/$', learn_views.test),
    url(r'^test_form/$', learn_views.test_form),

    # http://127.0.0.1:8000/blog_info
    url(r'^blog_info/$', learn_views.query_blog_info),
]
