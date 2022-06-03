from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "students_attendance_app.AdminView":
                    pass
                elif modulename == "students_attendance_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse('admin_home'))
            elif user.user_type == "2":
                if modulename == "students_attendance_app.TeacherView":
                    pass
                elif modulename == "students_attendance_app.views"  or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse('teacher_home'))
            else:
                return HttpResponseRedirect(reverse('show_login'))
        else:
            if request.path == reverse('show_login') or request.path == reverse('doLogin') or modulename == 'django.contrib.auth.urls':
                pass
            else:
                return HttpResponseRedirect(reverse('show_login'))