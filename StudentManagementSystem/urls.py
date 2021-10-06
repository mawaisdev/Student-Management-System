"""StudentManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from StudentManagementApp import views
from StudentManagementApp import HODViews
from StudentManagementSystem import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', views.showDemoPage),
    path("", views.login_user),
    path("getUserDetails", views.GetUserDetails),
    path("logout_user", views.logout_user),
    path("dologin", views.dologin),
    path('admin_home',HODViews.admin_home),
    path('add_staff',HODViews.add_staff),
    path('add_staff_save',HODViews.add_staff_save),
    path('add_course_save',HODViews.add_course_save),
    path('add_course',HODViews.add_course),
    path('add_student_save',HODViews.add_student_save),
    path('add_student',HODViews.add_student),
    path('add_subject_save',HODViews.add_subject_save),
    path('add_subject',HODViews.add_subject),
    path('manage_staff',HODViews.manage_staff),
    path('manage_student',HODViews.manage_student),
    path('manage_course',HODViews.manage_course),
    path('manage_subject',HODViews.manage_subject),
    # Here accessing staff ID by URL that's why i added string variable in the path end
    # patth/<DATATYPE:VARIABLE>
    path('edit_staff/<str:staff_id>',HODViews.edit_staff),
    path('edit_staff_save',HODViews.edit_staff_save),
    path('edit_student/<str:student_id>',HODViews.edit_student),
    path('edit_student_save',HODViews.edit_student_save)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,
                                                                       document_root=settings.STATIC_ROOT)
