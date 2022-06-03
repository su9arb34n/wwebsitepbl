"""websitePBL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf.urls.static import static

from websitePBL import settings
from students_attendance_app import AdminView, views, TeacherView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.showLogin, name="show_login"),
    path('get_user_details/', views.GetUserDetails),
    path('logout_user/', views.logout_user, name="logout"),
    path('doLogin', views.doLogin, name="doLogin"),
    # Admin URL path
    path('admin_home', AdminView.admin_home, name="admin_home"),
    path('add_teacher', AdminView.add_teacher, name="add_teacher"),
    path('add_teacher_save', AdminView.add_teacher_save, name="add_teacher_save"),
    path('add_subject', AdminView.add_subject, name="add_subject"),
    path('add_subject_save', AdminView.add_subject_save, name="add_subject_save"),
    path('add_student', AdminView.add_student, name="add_student"),
    path('add_student_save', AdminView.add_student_save, name="add_student_save"),
    path('add_classes', AdminView.add_classes, name="add_classes"),
    path('add_classes_save', AdminView.add_classes_save, name="add_classes_save"),
    path('add_department', AdminView.add_department, name="add_department"),
    path('add_department_save', AdminView.add_department_save, name="add_department_save"),
    path('manage_teacher', AdminView.manage_teacher, name="manage_teacher"),
    path('manage_student', AdminView.manage_student, name="manage_student"),
    path('manage_subject', AdminView.manage_subject, name="manage_subject"),
    path('manage_classes', AdminView.manage_classes, name="manage_classes"),
    path('manage_department', AdminView.manage_department, name="manage_department"),
    path('edit_teacher/<str:teacher_id>', AdminView.edit_teacher, name="edit_teacher"),
    path('edit_teacher_save', AdminView.edit_teacher_save, name="edit_teacher_save"),
    path('edit_student/<str:student_id>', AdminView.edit_student, name="edit_student"),  
    path('edit_student_save', AdminView.edit_student_save, name="edit_student_save"),
    path('edit_subject/<str:subject_id>', AdminView.edit_subject, name="edit_subject"),
    path('edit_subject_save', AdminView.edit_subject_save, name="edit_subject_save"),
    path('edit_classes/<str:classes_id>', AdminView.edit_classes, name="edit_classes"),
    path('edit_classes_save', AdminView.edit_classes_save, name="edit_classes_save"),
    path('edit_department/<str:department_id>', AdminView.edit_department, name="edit_department"),
    path('edit_department_save', AdminView.edit_department_save, name="edit_department_save"),
    path('delete_student/<str:student_id>', AdminView.delete_student, name="delete_student"),
    path('delete_classes/<str:classes_id>', AdminView.delete_classes, name="delete_classes"),
    path('delete_teacher/<str:teacher_id>', AdminView.delete_teacher, name="delete_teacher"),
    path('delete_department/<str:department_id>', AdminView.delete_department, name="delete_department"),
    path('delete_subject/<str:subject_id>', AdminView.delete_subject, name="delete_subject"),

    path('view_class_department/<str:department_id>', AdminView.view_class_department, name="view_class_department"),
    path('view_attendance/<str:classes_id>', AdminView.view_attendance, name="view_attendance"),
    path('edit_attendance/<str:attendance_id>', AdminView.edit_attendance, name="edit_attendance"),
    path('edit_attendance_save', AdminView.edit_attendance_save, name="edit_attendance_save"),
    path('add_student_attendance/<str:lophocphan_id>', AdminView.add_student_attendance, name="add_student_attendance"),
    path('add_student_attendance_save', AdminView.add_student_attendance_save, name="add_student_attendance_save"),
    path('remove_student_attendance/<str:attendance_id>', AdminView.remove_student_attendance, name="remove_student_attendance"),
    path('export_excel/<str:lophocphan_id>', views.export_excel, name="export_excel"),
    # Teacher URL path
    path('teacher_home', TeacherView.teacher_home, name="teacher_home"),
    path('view_attendance_teacher/<str:classes_id>', TeacherView.view_attendance_teacher, name="view_attendance_teacher"),
    path('view_classes', TeacherView.view_classes, name="view_classes"),
    path('edit_attendance_teacher/<str:attendance_id>', TeacherView.edit_attendance_teacher, name="edit_attendance_teacher"),
    path('edit_attendance_teacher_save', TeacherView.edit_attendance_teacher_save, name="edit_attendance_teacher_save"),
    path('view_student_info/<str:classes_id>', TeacherView.view_student_info, name="view_student_info"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
