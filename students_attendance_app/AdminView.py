from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from students_attendance_app import admin
from students_attendance_app.models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from .forms import AddStudentForm, EditStudentForm
from django.urls import reverse
import re

def admin_home(request):
    total_gv = GiangVien.objects.all().count()
    total_sv = SinhVien.objects.all().count()
    total_khoa = Khoa.objects.all().count()
    totl_lhp = LopHocPhan.objects.all().count()
    return render(request, 'admin_template/home_content.html', {'total_sv': total_sv, 'total_khoa': total_khoa, 'total_gv': total_gv, 'total_lhp': totl_lhp})

def add_teacher(request):
    khoas = Khoa.objects.all()
    return render(request, 'admin_template/add_teacher_template.html', {'khoas': khoas})

def add_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        sex = request.POST.get("sex")
        department = request.POST.get("department")
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password, last_name=last_name, first_name=first_name, user_type=2)
            user.giangvien.gioitinh = sex
            user.giangvien.email = email
            user.giangvien.ten_gv = str(first_name + " " + last_name)
            user.giangvien.khoa_id = department
            user.giangvien.save()
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Thêm giảng viên thành công')
            return HttpResponseRedirect(reverse("add_teacher"))
        except:
            messages.add_message(request, messages.ERROR, 'Thêm giảng viên thất bại')
            return HttpResponseRedirect(reverse("add_teacher"))
        
def add_subject(request):
    return render(request, 'admin_template/add_subject_template.html')

def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        id = request.POST.get('id')
        subject_name = request.POST.get('subject_name')
        description = request.POST.get('description')
        try:
            list_id = MonHoc.objects.all().values_list('name', flat=True)
            if id in list_id:
                messages.add_message(request, messages.ERROR, 'ID môn học đã tồn tại')
                return HttpResponseRedirect(reverse("add_subject"))
            else:
                monhoc = MonHoc(id=id, ten_mon=subject_name, mo_ta=description)
                monhoc.save()
                messages.add_message(request, messages.SUCCESS, 'Thêm môn học thành công')
                return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.add_message(request, messages.ERROR, 'Thêm môn học thất bại')
            return HttpResponseRedirect(reverse("add_subject"))

def add_student(request):
    form = AddStudentForm()
    return render(request, 'admin_template/add_student_template.html', {'form': form})

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            department = form.cleaned_data['department']
            sex = form.cleaned_data['sex']

            profile_pic = request.FILES.get('profile_pic')
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        
            try:
                list_id = SinhVien.objects.all().values_list('id', flat=True)
                if id in list_id:
                    messages.add_message(request, messages.ERROR, 'ID sinh viên đã tồn tại')
                    return HttpResponseRedirect(reverse("add_student"))
                else:
                    sinhvien = SinhVien(id=id, ten_sv=name, khoa_id=department, gioitinh=sex, anhthe=profile_pic_url)
                    sinhvien.save()
                    messages.add_message(request, messages.SUCCESS, 'Thêm sinh viên thành công')
                    return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.add_message(request, messages.ERROR, 'Thêm sinh viên thất bại')
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form = AddStudentForm(request.POST)
            return render(request, 'admin_template/add_student_template.html', {'form': form})


   
def add_classes(request):
    giangvien = GiangVien.objects.all()
    monhoc = MonHoc.objects.all()
    khoa  = Khoa.objects.all()
    return render(request, 'admin_template/add_classes_template.html', {'giangviens': giangvien, 'monhocs': monhoc, 'khoas': khoa})

def add_classes_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        group = request.POST.get('group')
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        subject = request.POST.get('subject')
        session = request.POST.get('session')
        department = request.POST.get('department')
        id = department + subject + "." + group
        try:
            list_id = LopHocPhan.objects.all().values_list('id', flat=True)
            if id in list_id:
                messages.add_message(request, messages.ERROR, 'Lớp học phần đã tồn tại')
                return HttpResponseRedirect(reverse("add_classes"))
            else:
                lophocphan = LopHocPhan(id=id, ten_lophp=name, kyhoc=session, giangvien_id=teacher, mon_id=subject)
                lophocphan.save()
                messages.add_message(request, messages.SUCCESS, 'Thêm lớp học phần thành công')
                return HttpResponseRedirect(reverse("add_classes"))
        except:
            messages.add_message(request, messages.ERROR, 'Thêm lớp học phần thất bại')
            return HttpResponseRedirect(reverse("add_classes"))

def add_department(request):
    return render(request, 'admin_template/add_department_template.html')

def add_department_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        try:
            list_id = Khoa.objects.all().values_list('id', flat=True)
            if id in list_id:
                messages.add_message(request, messages.ERROR, 'ID khoa đã tồn tại')
                return HttpResponseRedirect(reverse("add_department"))
            else:
                khoa = Khoa(id=id, tenkhoa=name)
                khoa.save()
                messages.add_message(request, messages.SUCCESS, 'Thêm khoa thành công')
                return HttpResponseRedirect(reverse("add_department"))
        except:
            messages.add_message(request, messages.ERROR, 'Thêm khoa thất bại')
            return HttpResponseRedirect(reverse("/add_department"))

def manage_teacher(request):
    teacher = GiangVien.objects.all()
    khoa = Khoa.objects.all()
    return render(request,'admin_template/manage_teacher_template.html', {'teachers': teacher, 'khoas': khoa})

def manage_student(request):
    student = SinhVien.objects.all()
    khoa = Khoa.objects.all()
    return render(request,'admin_template/manage_student_template.html', {'students': student, 'khoas': khoa})

def manage_subject(request):
    subject = MonHoc.objects.all()
    return render(request,'admin_template/manage_subject_template.html', {'subjects': subject})

def manage_classes(request):
    classes = LopHocPhan.objects.all()
    teacher = GiangVien.objects.all()
    subject = MonHoc.objects.all()
    return render(request,'admin_template/manage_classes_template.html', {'classes': classes, 'teachers': teacher, 'subjects': subject})

def manage_department(request):
    department = Khoa.objects.all()
    return render(request,'admin_template/manage_department_template.html', {'departments': department})

def edit_teacher(request, teacher_id):
    teacher = GiangVien.objects.get(admin=teacher_id)
    khoa = Khoa.objects.all()
    return render(request,'admin_template/edit_teacher_template.html', {'teacher': teacher, 'khoas': khoa, "id": teacher_id})

def edit_teacher_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        teacher_id = request.POST.get('teacherAdmin_id')
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        name = str(first_name + " " + last_name)
        sex = request.POST.get('sex')

        try:
            user = CustomUser.objects.get(id = teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            teacher_models = GiangVien.objects.get(admin=teacher_id)
            teacher_models.ten_gv = name
            teacher_models.khoa_id = department
            teacher_models.gioitinh = sex
            teacher_models.email = email
            teacher_models.save()

            messages.add_message(request, messages.SUCCESS, 'Cập nhật thông tin thành công')
            return HttpResponseRedirect(reverse("edit_teacher",kwargs={'teacher_id':teacher_id}))
        except:
            messages.add_message(request, messages.ERROR, 'Cập nhật thông tin thất bại')
            return HttpResponseRedirect(reverse("edit_teacher",kwargs={'teacher_id':teacher_id}))

def edit_student(request, student_id):
    request.session['student_id'] = student_id
    student = SinhVien.objects.get(id=student_id)
 
    form = EditStudentForm()
    form.fields['name'].initial = student.ten_sv
    form.fields['department'].initial = student.khoa_id
    form.fields['sex'].initial = student.gioitinh
    form.fields['profile_pic'].initial = student.anhthe

    return render(request,'admin_template/edit_student_template.html', {"form": form, "id": student_id})


def edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        student_id = request.session.get('student_id')
        if student_id==None:
            return HttpResponseRedirect(reverse("manage_student"))

        form = EditStudentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            department = form.cleaned_data['department']
            sex = form.cleaned_data['sex']

            if request.FILES.get('profile_pic',False):
                profile_pic = request.FILES.get('profile_pic')
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                student = SinhVien.objects.get(id = student_id)
                student.ten_sv = name
                student.gioitinh = sex
                student.khoa_id = department
                if profile_pic_url!=None:
                    student.anhthe = profile_pic_url
                student.save()
                del request.session['student_id']
                messages.add_message(request, messages.SUCCESS, 'Cập nhật thông tin thành công')
                return HttpResponseRedirect(reverse("edit_student",kwargs={'student_id':student_id}))
            except:
                messages.add_message(request, messages.ERROR, 'Cập nhật thông tin thất bại')
                return HttpResponseRedirect(reverse("edit_student",kwargs={'student_id':student_id}))
        else:
            form = EditStudentForm(request.POST)
            student = SinhVien.objects.get(id=student_id)
            return render(request,'admin_template/edit_student_template.html', {"form": form, "id": student_id})




def edit_subject(request, subject_id):
    subject = MonHoc.objects.get(id=subject_id)
    return render(request,'admin_template/edit_subject_template.html', {'subject': subject, "id": subject_id})

def edit_subject_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        id = request.POST.get('subject_id')
        subject_name = request.POST.get('name')
        description = request.POST.get('description')
        try:
            monhoc = MonHoc.objects.get(id=id)
            monhoc.ten_mon = subject_name
            monhoc.mo_ta = description
            monhoc.save()
            messages.add_message(request, messages.SUCCESS, 'Cập nhật thông tin thành công')
            return HttpResponseRedirect(reverse("edit_subject",kwargs={'subject_id':id}))
        except:
            messages.add_message(request, messages.ERROR, 'Cập nhật thông tin thất bại')
            return HttpResponseRedirect(reverse("edit_subject",kwargs={'subject_id':id}))

def edit_classes(request, classes_id):
    classes = LopHocPhan.objects.get(id=classes_id)
    teacher = GiangVien.objects.all()
    subject = MonHoc.objects.all()
    return render(request,'admin_template/edit_classes_template.html', {'classes': classes, 'teachers': teacher, 'subjects': subject, "id": classes_id})

def edit_classes_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        session = request.POST.get('session')
        teacher = request.POST.get('teacher')
        subject = request.POST.get('subject')
        try:
            lophocphan = LopHocPhan.objects.get(id=id)
            lophocphan.ten_lophp = name
            lophocphan.kyhoc = session
            lophocphan.giangvien_id = teacher
            lophocphan.mon_id = subject
            lophocphan.save()

            messages.add_message(request, messages.SUCCESS, 'Cập nhật thông tin thành công')
            return HttpResponseRedirect(reverse("edit_classes",kwargs={'classes_id':id}))
        except:
            messages.add_message(request, messages.ERROR, 'Cập nhật thông tin thất bại')
            return HttpResponseRedirect(reverse("edit_classes",kwargs={'classes_id':id}))

def edit_department(request, department_id):
    department = Khoa.objects.get(id=department_id)
    return render(request,'admin_template/edit_department_template.html', {'department': department, "id": department_id})

def edit_department_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        id = request.POST.get('department_id')
        name = request.POST.get('name')
        try:
            khoa = Khoa.objects.get(id=id)
            khoa.tenkhoa = name
            khoa.save()

            messages.add_message(request, messages.SUCCESS, 'Cập nhật thông tin thành công')
            return HttpResponseRedirect(reverse("edit_department",kwargs={'department_id':id}))
        except:
            messages.add_message(request, messages.ERROR, 'Cập nhật thông tin thất bại')
            return HttpResponseRedirect(reverse("edit_department",kwargs={'department_id':id}))


def delete_student(request, student_id):
    student = SinhVien.objects.get(id=student_id)
    try:
        student.delete()
        messages.add_message(request, messages.SUCCESS, 'Xóa thông tin sinh viên thành công')
        return redirect('manage_student')
    except:
       messages.add_message(request, messages.ERROR, 'Xóa thông tin sinh viên thất bại')
       return redirect('manage_student')
       

def delete_classes(request, classes_id):
    classes = LopHocPhan.objects.get(id=classes_id)
    try:
        classes.delete()
        messages.add_message(request, messages.SUCCESS, 'Xóa thông tin lớp học phần thành công')
        return redirect('manage_classes')
    except:
       messages.add_message(request, messages.ERROR, 'Xóa thông tin lớp học phần thất bại')
       return redirect('manage_classes')


def delete_teacher(request, teacher_id):
    teacher = GiangVien.objects.get(admin=teacher_id)
    user = CustomUser.objects.get(id = teacher_id)
    try:
        user.delete()
        teacher.delete()
        messages.add_message(request, messages.SUCCESS, 'Xóa thông tin giảng viên thành công')
        return redirect('manage_teacher')
    except:
       messages.add_message(request, messages.ERROR, 'Xóa thông tin giảng viên thất bại')
       return redirect('manage_teacher')


def delete_department(request, department_id):
    department = Khoa.objects.get(id=department_id)
    try:
        department.delete()
        messages.add_message(request, messages.SUCCESS, 'Xóa thông tin khoa thành công')
        return redirect('manage_department')
    except:
       messages.add_message(request, messages.ERROR, 'Xóa thông tin khoa thất bại')
       return redirect('manage_department')


def delete_subject(request, subject_id):
    subject = MonHoc.objects.get(id=subject_id)
    try:
        subject.delete()
        messages.add_message(request, messages.SUCCESS, 'Xóa thông tin môn học thành công')
        return redirect('manage_subject')
    except:
       messages.add_message(request, messages.ERROR, 'Xóa thông tin môn học thất bại')
       return redirect('manage_subject')


def view_class_department(request, department_id):
    my_regex = r'^(' + department_id + ')+'
    classes = LopHocPhan.objects.filter(id__regex=my_regex)
    teacher = GiangVien.objects.all()
    subject = MonHoc.objects.all()
    name_department = Khoa.objects.values_list('tenkhoa', flat=True).filter(id=department_id)[0]

    return render(request,'admin_template/view_class_department.html', {'classes': classes, 'teachers': teacher, 'subjects': subject, 'name_department': name_department})

def view_attendance(request, classes_id):
    classes = LopHocPhan.objects.get(id=classes_id)
    attendance = DiemDanh.objects.filter(lophocphan_id=classes_id)
    teacher = GiangVien.objects.get(id=classes.giangvien_id)
    student = SinhVien.objects.all()
    return render(request, 'admin_template/view_attendance.html', {'classes': classes, 'attendance': attendance, 'teacher': teacher, 'students': student})

def edit_attendance(request, attendance_id):
    context = {
        'students': SinhVien.objects.all(),
        'student_at': DiemDanh.objects.get(id=attendance_id),
        'classes': LopHocPhan.objects.all()
    }
    return render(request, 'admin_template/edit_attendance.html', context)

def edit_attendance_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        id = request.POST.get('id')
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
        next = request.POST.get('next', '/')
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
            return HttpResponseRedirect(reverse('edit_attendance', kwargs={'attendance_id': id}))


def add_student_attendance(request, lophocphan_id):
    students = SinhVien.objects.exclude(id__in = DiemDanh.objects.filter(lophocphan_id=lophocphan_id).values_list('sinhvien_id').distinct()).all()
    classes = LopHocPhan.objects.get(id=lophocphan_id)
    context = {
        'students': students,
        'classes': classes
    }

    return render(request, 'admin_template/add_student_attendance.html', context)

def add_student_attendance_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        lophocphan_id = request.POST.get('lophocphan_id')
        student_id = request.POST.get('student_id')
        try:
            sinhvien = DiemDanh.objects.create(lophocphan_id=lophocphan_id, sinhvien_id=student_id)
            sinhvien.save()

            return HttpResponseRedirect(reverse('view_attendance', kwargs={'classes_id': lophocphan_id}))
        except:
            messages.add_message(request, messages.ERROR, 'Thêm thất bại')
            return HttpResponseRedirect(reverse('add_student_attendance', kwargs={'lophocphan_id': lophocphan_id}))

def remove_student_attendance(request, attendance_id):
    try:
        attendance = DiemDanh.objects.get(id=attendance_id)
        attendance.delete()
        return HttpResponseRedirect(reverse('view_attendance', kwargs={'classes_id': attendance.lophocphan_id}))
    except:
       return HttpResponseRedirect(reverse('view_attendance', kwargs={'classes_id': attendance.lophocphan_id}))

