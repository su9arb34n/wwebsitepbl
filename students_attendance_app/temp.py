from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, 'Admin'), (2, 'Teacher'))
    user_type = models.CharField(default = 1, choices = user_type_data, max_length = 10)

# Table Admin
class AdminHOD(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Student_FacePrint(models.Model):
    id = models.AutoField(primary_key=True)
    id_student_faceprint = models.CharField(max_length=10)
    embedding = models.CharField(max_length=128)

class Student_Embeddings(models.Model):
    id = models.AutoField(primary_key=True)
    id_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    # id_student_faceprint = models.ManyToManyField(Student_FacePrint)
    embedding = models.CharField(max_length=128)

# Khoa
class Department(models.Model):
    id_department = models.CharField(max_length=10, primary_key=True)
    name_department = models.CharField(max_length=255)

# Giao vien
class Teacher(models.Model):
    id_teacher = models.CharField(max_length=10, primary_key=True)
    user_type = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # name_teacher = models.CharField(max_length=255)
    sex = models.CharField(max_length=3)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)


# Sinh vien
class Student(models.Model):
    id_student = models.CharField(max_length=10, primary_key=True)
    name_student = models.CharField(max_length=255)
    sex = models.CharField(max_length=3)
    student_pic = models.URLField(max_length=255)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_section = models.ForeignKey('Class_Section', on_delete=models.CASCADE)
    
# LOP HOC PHAN (CBI SUA)
class Class_Section(models.Model):
    id_class = models.CharField(max_length=10, primary_key=True)
    name_class = models.CharField(max_length=255)
    semester = models.CharField(max_length=255) # Ky hoc
    students = models.ManyToManyField(Student, related_name="class_section_students")
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    

#MON - n lop hoc phan thuoc ve 1 mon, 1 mon thuoc ve nhieu lop hp
class Subject(models.Model):
    id_subject = models.CharField(max_length=10, primary_key=True)
    name_subject = models.CharField(max_length=255)
    id_class = models.ForeignKey(Class_Section, on_delete=models.CASCADE)

class List_Students(models.Model):
    id = models.AutoField(primary_key=True)
    stt = models.IntegerField(auto_created=True)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_section = models.OneToOneField(Class_Section, on_delete=models.CASCADE)
    day_1 = models.BooleanField(default=False)
    day_2 = models.BooleanField(default=False)
    day_3 = models.BooleanField(default=False)
    day_4 = models.BooleanField(default=False)
    day_5 = models.BooleanField(default=False)
    day_6 = models.BooleanField(default=False)
    day_7 = models.BooleanField(default=False) 
    day_8 = models.BooleanField(default=False)
    day_9 = models.BooleanField(default=False)
    day_10 = models.BooleanField(default=False)
    day_11 = models.BooleanField(default=False)
    day_12 = models.BooleanField(default=False)
    day_13 = models.BooleanField(default=False)
    day_14 = models.BooleanField(default=False)
    day_15 = models.BooleanField(default=False)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Teacher.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.teacher.save()
