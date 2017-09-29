"""
    admin.site.register()  -- 只有通过该方法才能在admin页面看到

    说明文档
        https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
"""
from django.contrib import admin
from .models import Article, Author, Person

admin.site.register(Article)
admin.site.register(Person)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)  # 列表显示(list_display) 用逗号隔开
    search_fields = ('name', 'email')  # 搜索功能(search_fields) 支持模糊搜索
    list_filter = ('name',)  # 根据name来过滤 页面会显示过滤器 by name

    # get_queryset方法 (根据不同权限设置显示内容)
    def get_queryset(self, request):
        qs = super(AuthorAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # admin管理员
            return qs
        else:
            # 其他用户(仅能访问自己相关)
            return qs.filter(email=request.user)

    # 修改保存时的一些操作 (保存时加上添加人)
    # obj--修改后的对象
    # form--修改后的表单
    # change--新建对象为False, 修改对象时为True
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Author, AuthorAdmin)
