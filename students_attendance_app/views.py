
from tkinter import font
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from students_attendance_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from students_attendance_app.models import *
from django.urls import reverse
import datetime
import xlwt
import numpy as np
# Create your views here.
def search_student(request):
    if request.method != 'GET':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        if request.user.user_type == "1":
            return render(request, 'admin_search_student.html')


def showLogin(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user!=None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("teacher_home"))
        else:
            messages.error(request, 'Invalid Login Credentials!')
            return HttpResponseRedirect("/")
            
def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + " user_type: " + request.user.user_type)
    else:
        return HttpResponse("Please login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


def export_excel(request, lophocphan_id):
    if request.method != 'GET':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        response =HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename=DiemDanh-' + lophocphan_id + '-' + \
            str(datetime.datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding="utf-8")
        ws = wb.add_sheet("Điểm danh")

        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['MSSV', 'Buổi 1', 'Buổi 2', 'Buổi 3', 'Buổi 4', 'Buổi 5',
                'Buổi 6', 'Buổi 7', 'Buổi 8', 'Buổi 9', 'Buổi 10',
                'Buổi 11', 'Buổi 12', 'Buổi 13', 'Buổi 14', 'Buổi 15']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
    
        font_style = xlwt.XFStyle()
        data=DiemDanh.objects.filter(lophocphan_id=lophocphan_id).values_list('sinhvien_id', 'buoi_1', 'buoi_2', 'buoi_3', 'buoi_4',
                                'buoi_5', 'buoi_6', 'buoi_7', 'buoi_8', 'buoi_9', 'buoi_10','buoi_11', 'buoi_12', 'buoi_13', 'buoi_14', 'buoi_15')
        rows = []
        for i in range(len(data)):
            for j in range(16):
                if data[i][j]==True:
                    rows.append(["C"])
                elif data[i][j]==False:
                    rows.append(["V"])
                else:
                    rows.append([data[i][j]])

        rows = np.reshape(rows,(len(data),16))
        for row in rows:
            row_num+=1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)
        return response        
