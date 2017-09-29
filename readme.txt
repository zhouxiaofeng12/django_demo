Django 环境搭建
    一、新建django project(需要切换到%PYTHON_HOME%\Lib\site-packages\Django-1.11.5-py3.6.egg\django\bin)
        django-admin startproject project_name

    二、新建app(需要切换到project_name下)
        cd project_name
        python manage.py startapp app_name
        [新定义的app加到settings.py中的INSTALL_APPS中]

        一个项目一般包含多个应用，一个应用也可以用在多个项目中

    三、创建数据库表
        # 1. 创建更改的文件
        python manage.py makemigrations
        # 2. 将生成的py文件应用到数据库


    四、使用开发服务器
        python manage.py runserver ip:端口号

    五、数据库相关操作
        python manage.py makemigrations # 创建migrations 用于将models中的类映射成表
        python manage.py migrate # 同步数据库
        python manage.py flush # 清空数据库

========================================================================================
Django 模板查找机制
    模板一般放在app下的templates中，Django会自动去这个文件夹中找
    查找模板的过程是在每个app的templates文件夹中找
        各个app的templates形成一个文件夹列表，
        Django遍历这个列表，一个个进行查找，当在某一个文件夹找到的时候就停止，
        所有的都遍历完了还找不到指定的模板的时提示Template Not Found

    好处:一个app可以用另一个app的模板文件
    坏处:同名的文件夹会发生错误
    解决方法: 模板放在 app/templates/app/ 目录下

========================================================================================
    变量	                        描述
forloop.counter	            索引从 1 开始算
forloop.counter0	        索引从 0 开始算
forloop.revcounter	        索引从最大长度到 1
forloop.revcounter0	        索引从最大长度到 0
forloop.first	            当遍历的元素为第一项时
forloop.last	            当遍历的元素为最后一项时
forloop.parentloop	        用在嵌套的 for 循环中，获取上一层 for 循环的 forloop

========================================================================================
Django的admin功能

 一、创建admin    python manage.py createsuperuser
        账号:shijie9
        邮箱:kuangye89757@163.com
        密码:1234!@#$

    之后会在auth_user表中插入数据

 二、进入people文件夹修改admin.py（如果没有新建一个）内容如下;
    from django.contrib import admin
    from .models import Article

    admin.site.register(Article)

 三、之后访问http://localhost:8000/admin/
        User中添加新用户(普通用户) 并根据需要设置权限 (这里同时选中staff status否则无法访问admin页)
            账号:12@163.com
            密码:zhoufeng666

 四、点击Home › People › Articles › ADD ARTICLE
    强大的后台会根据我们定义在models.py的Article类创建对应的界面


 五、通过admin.py中
        admin.site.register(Model类名) 页面则显示相应的数据

 六、在model上添加注解标签@python_2_unicode_compatible 用来兼容python2和3

    栗子：

        from django.utils.encoding import python_2_unicode_compatible


        @python_2_unicode_compatible
        class Author(models.Model):
            name = models.CharField(max_length=50)
            qq = models.CharField(max_length=10)
            address = models.TextField()
            email = models.EmailField()

            def __str__(self):
                return str(self.name) + " / " + str(self.email)