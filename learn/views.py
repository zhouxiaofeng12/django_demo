# -*- coding: utf-8 -*-
"""
    定义视图函数（访问页面时的内容）
    定义了一个index()函数，第一个参数必须是request(与网页请求有关)
    返回了一个HttpResponse对象
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# 首页
from django.urls import reverse


def index(request):
    return HttpResponse("Welcome!")


# home页
def home(request):
    """
        使用render时，Django会自动找到settings.py的INSTALLED_APPS所列出的各个app下templates中的文件
    """
    return render(request, 'learn/home.html')


# 加法
def add(request):
    a = request.POST.get('a', '22')  # 无论有没有传递a 默认都为22
    b = request.GET['b']  # request.GET 类似于一个字典
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 查询第几页
def query(request, page):
    return HttpResponse(str('查询第' + page + '页数据'))


# 页面重定向
def page_redirect(request, page):
    """
        等价于使用{% url 'new_page' 参数 %}
    """
    return HttpResponseRedirect(
        reverse('new_page', args=(page))
    )


# 查询第几页(新)
def new_query(request, page):
    return HttpResponse(str('新页面--查询第' + page + '页数据'))


# 模板页
def template(request):
    """
        使用render时，Django会自动找到settings.py的INSTALLED_APPS所列出的各个app下templates中的文件
    """
    render_dict = {}

    # 单一内容
    render_dict['template_content'] = 'This is template page'

    # 列表
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    render_dict['template_list'] = TutorialList

    # 字典
    info_dict = {'site': '嘿嘿', 'content': '哈哈'}
    render_dict['template_dict'] = info_dict

    # for循环
    lst = map(str, range(10))  # 一个长度为10的List
    render_dict['template_range'] = lst

    return render(request, 'learn/template.html', render_dict)
