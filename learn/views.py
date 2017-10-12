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
from learn.forms import AddForm, AddTestForm
from people.models import Blog


def index(request):
    return HttpResponse("Welcome!")


# home页
def home(request):
    """
        使用render时，Django会自动找到settings.py的INSTALLED_APPS所列出的各个app下templates中的文件
    """
    return render(request, 'learn/home.html')


def test(request):
    return render(request, 'learn/test.html')


# 加法
def add(request):
    a = request.GET.get('a', '22')  # 无论有没有传递a 默认都为22
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


# 表单页
def form(request):
    form_info = AddForm()
    return render(request, 'learn/form.html', {'form_info': form_info})


# 通过表单调用
def add_form(request):
    if request.method == 'POST':
        # post方式
        form_param = AddForm(request.POST)  # form 包含提交的数据
        if form_param.is_valid():  # 如果提交的数据合法
            a = form_param.cleaned_data['a']
            b = form_param.cleaned_data['b']
            return HttpResponse('This is post method ' + str(int(a) + int(b)))

    elif request.method == 'GET':
        # get方式
        a = request.GET['a']
        b = request.GET['b']
        return HttpResponse('This is get method ' + str(int(a) + int(b)))


def test_form(request):
    form_param = AddTestForm(request.POST)  # form 包含提交的数据
    if form_param.is_valid():  # 如果提交的数据合法
        name = form_param.cleaned_data['name']
        tag_line = form_param.cleaned_data['tag_line']
        b = Blog(name=name, tagline=tag_line)
        b.save()
        return HttpResponse('保存成功~!' + str(name) + str(tag_line))


# 查询blog表的数据
def query_blog_info(request):
    render_dict = {}
    render_dict['blog_info'] = Blog.objects.all()
    return render(request, 'learn/blog_info.html', render_dict)
