# -*- coding: utf-8 -*-
from django.db import models


class Art(models.Model):
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
