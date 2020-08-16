"""Exam URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from onlineapp import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
   # path('dashboard/',views.dashboardView,name="dashboard"),
    path('t_dashboard/',views.t_dashboardView,name="t_dashboard"),
    path('s_dashboard/',views.s_dashboardView,name="s_dashboard"),

    path('select/', views.selectView, name="select"),

    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name="login"),

    path('register/',views.register,name="register"),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),

    path('student/', views.student_list, name='student_list'),
    path('teacher/', views.teacher_list, name='teacher_list'),

    path('student/upload/', views.upload_student, name='upload_student'),
    path('teacher/upload/', views.upload_teacher, name='upload_teacher'),

    path('teacher/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    path('student/<int:pk>/', views.delete_student, name='delete_student'),

    path('edit_student/<int:pk>', views.edit_student, name='edit_student'),
    path('edit_teacher/<int:pk>', views.edit_teacher, name='edit_teacher'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('update_teacher/<int:pk>', views.update_teacher, name='update_teacher'),

    path('admin/', admin.site.urls),
]