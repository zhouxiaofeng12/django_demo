# -*- coding: utf-8 -*-
"""
    部署服务器时用到的文件
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_demo.settings")

application = get_wsgi_application()
