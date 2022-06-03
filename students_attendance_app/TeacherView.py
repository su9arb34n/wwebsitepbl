from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from students_attendance_app.models import *
from django.contrib import messages
from django.urls import reverse


def teacher_home(request):
    classes = LopHocPhan.objects.filter(giangvien_id=int(request.user.id - 1))
    return render(request, 'teacher_template/teacher_home_template.html', {'classes': classes})

def view_attendance_teacher(request, classes_id):
    classes = LopHocPhan.objects.get(id=classes_id)
    attendance = DiemDanh.objects.filter(lophocphan_id=classes_id)
    teacher = GiangVien.objects.get(id=classes.giangvien_id)
    student = SinhVien.objects.all()
    return render(request, 'teacher_template/view_attendance.html', {'classes': classes, 'attendance': attendance, 'teacher': teacher, 'students': student})

def view_classes(request):
    classes = LopHocPhan.objects.filter(giangvien_id=int(request.user.id - 1))
    teacher = GiangVien.objects.all()
    subject = MonHoc.objects.all()
    return render(request,'teacher_template/view_classes.html', {'classes': classes, 'teachers': teacher, 'subjects': subject})

def edit_attendance_teacher(request, attendance_id):
    context = {
        'students': SinhVien.objects.all(),
        'student_at': DiemDanh.objects.get(id=attendance_id),
        'classes': LopHocPhan.objects.all()
    }
    return render(request, 'teacher_template/edit_attendance.html', context)

def edit_attendance_teacher_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        id = request.POST.get('id')
        next = request.POST.get('next', '/')
        buoi_1 = request.POST.get('buoi_1')
        buoi_2 = request.POST.get('buoi_2')
        buoi_3 = request.POST.get('buoi_3')
        buoi_4 = request.POST.get('buoi_4')
        buoi_5 = request.POST.get('buoi_5')
        buoi_6 = request.POST.get('buoi_6')
        buoi_7 = request.POST.get('buoi_7')
        buoi_8 = request.POST.get('buoi_8')
        buoi_9 = request.POST.get('buoi_9')
        buoi_10 = request.POST.get('buoi_10')
        buoi_11 = request.POST.get('buoi_11')
        buoi_12 = request.POST.get('buoi_12')
        buoi_13 = request.POST.get('buoi_13')
        buoi_14 = request.POST.get('buoi_14')
        buoi_15 = request.POST.get('buoi_15')
        try:
            sinhvien = DiemDanh.objects.get(id=id)
            sinhvien.buoi_1=buoi_1
            sinhvien.buoi_2=buoi_2
            sinhvien.buoi_3=buoi_3
            sinhvien.buoi_4=buoi_4
            sinhvien.buoi_5=buoi_5
            sinhvien.buoi_6=buoi_6
            sinhvien.buoi_7=buoi_7
            sinhvien.buoi_8=buoi_8
            sinhvien.buoi_9=buoi_9
            sinhvien.buoi_10=buoi_10
            sinhvien.buoi_11=buoi_11
            sinhvien.buoi_12=buoi_12
            sinhvien.buoi_13=buoi_13
            sinhvien.buoi_14=buoi_14
            sinhvien.buoi_15=buoi_15
            sinhvien.save()

            return HttpResponseRedirect(next)

        except:
            messages.add_message(request, messages.ERROR, 'Cập nhật thông tin thất bại')
            return HttpResponseRedirect(reverse('edit_attendance_teacher', kwargs={'attendance_id': id}))

