from students_attendance_app.models import *

def khoa_context(request):
    return {'khoa_context': Khoa.objects.all()}