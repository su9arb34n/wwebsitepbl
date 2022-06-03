from students_attendance_app.models import *

def khoa_context(request):
    return {'khoa_context': Khoa.objects.all()}

def get_list_subjects_teacher(request):
    if request.user.id == None:
        return []
    else:
        list_id_group = []
        for id_class in LopHocPhan.objects.filter(giangvien_id=int(request.user.id - 1)).values_list('id', flat=True):
            temp = id_class.split('.')[1] + '.' + id_class.split('.')[2]
            if not temp in list_id_group:
                list_id_group.append(temp)

        return {
            'list_id_subjects': LopHocPhan.objects.filter(giangvien_id=int(request.user.id - 1)).values_list('mon_id', flat=True).distinct(),
            'list_classes': LopHocPhan.objects.filter(giangvien_id=int(request.user.id -1)),
            'list_subjects': MonHoc.objects.all(),
            'list_id_group': list_id_group,
        }


    



