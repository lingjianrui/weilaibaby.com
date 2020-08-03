"""mother URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from app.views import *
from django.conf import settings
from app.upload import upload_image
from django.views.static import serve

urlpatterns = [
                  # 上传文件的路由配置
                  url(r"^uploads/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, }),
                  # 用于映射富文本编辑器的图片上传
                  url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', index, name='index'),
                  url(r'^map/$', map, name='map'),
                  url(r'^article/([^\s]+)/$', article, name='article'),
                  url(r'^markdownx/', include('markdownx.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
