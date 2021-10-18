"""StudentV4BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.get_students),  # 获取学生信息
    path('students/query/', views.query_students),  # 查询学生信息
    path('sno/check/', views.is_Exist_Sno),  # 查询学号信息
    path('student/add/', views.add_Student),  # 添加学生
    path('student/update/', views.update_Student),  # 更新学生
    path('student/delete/', views.delete_Student),  # 删除一个学生
    path('students/delete/', views.delete_Students),  # 删除一批学生
    path('upload/', views.upload),  # 上传照片
]

#添加这行--- 允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)