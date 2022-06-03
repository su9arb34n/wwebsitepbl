from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, 'Admin'), (2, 'Teacher'))
    user_type = models.CharField(default = 1, choices = user_type_data, max_length = 10)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            GiangVien.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.giangvien.save()

class AdminHOD(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

class Khoa(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    tenkhoa = models.CharField(max_length=255)
    objects = models.Manager()


class GiangVien(models.Model):
    # id = models.CharField(primary_key=True, max_length=10)
    id = models.AutoField(primary_key=True)
    khoa = models.ForeignKey(Khoa, on_delete=models.SET_NULL, null=True)
    ten_gv = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    gioitinh = models.CharField(max_length=3, null=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

class SinhVien(models.Model):
    id= models.CharField(max_length=10, primary_key=True)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE, null=True, blank=True)
    ten_sv = models.CharField(max_length=128)
    gioitinh = models.CharField(max_length=3)
    anhthe = models.FileField(null=True)
    objects = models.Manager()
    

class MonHoc(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    ten_mon = models.CharField(max_length=255)
    mo_ta = models.CharField(max_length=255, null=True)


class LopHocPhan(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    giangvien = models.ForeignKey(GiangVien,on_delete=models.CASCADE)
    mon = models.ForeignKey(MonHoc, on_delete=models.CASCADE, null=True)
    ten_lophp = models.CharField(max_length=255)
    kyhoc = models.CharField(max_length=255)
    objects = models.Manager()

    def get_id_khoa(self):
        if not self.id:
            return ""
        file_path = self.id[0:3]
        return os.path.basename(file_path)

    def get_id_class(self):
        if not self.id:
            return ""
        file_path = self.id.split(".")[1] + "." + self.id.split(".")[2]
        return os.path.basename(file_path)


class DiemDanh(models.Model):
    id = models.AutoField(primary_key=True)
    sinhvien = models.ForeignKey(SinhVien,on_delete=models.CASCADE)
    lophocphan = models.ForeignKey(LopHocPhan,on_delete=models.CASCADE)
    buoi_1 = models.BooleanField(default=False)
    buoi_2 = models.BooleanField(default=False)
    buoi_3 = models.BooleanField(default=False)
    buoi_4 = models.BooleanField(default=False)
    buoi_5 = models.BooleanField(default=False)
    buoi_6 = models.BooleanField(default=False)
    buoi_7 = models.BooleanField(default=False) 
    buoi_8 = models.BooleanField(default=False)
    buoi_9 = models.BooleanField(default=False)
    buoi_10 = models.BooleanField(default=False)
    buoi_11 = models.BooleanField(default=False)
    buoi_12 = models.BooleanField(default=False)
    buoi_13 = models.BooleanField(default=False)
    buoi_14 = models.BooleanField(default=False)
    buoi_15 = models.BooleanField(default=False)
    objects = models.Manager()


class VectorDacTrung(models.Model):
    id = models.AutoField(primary_key=True)
    sinhvien = models.ForeignKey(SinhVien,on_delete=models.CASCADE)
    vector_dt = models.TextField(null=False)

