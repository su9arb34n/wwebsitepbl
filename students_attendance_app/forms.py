from attr import attrs
from django import forms
from students_attendance_app.models import Khoa

class AddStudentForm(forms.Form):
    id = forms.CharField(label="ID", max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(label="Name", max_length=250, widget=forms.TextInput(attrs={'class':'form-control'}))
    khoas = Khoa.objects.all()
    khoa_list = []
    for khoa in khoas:
        khoa_list.append((khoa.id, khoa.tenkhoa))
    department = forms.ChoiceField(label="Department", choices=khoa_list, widget=forms.Select(attrs={'class':'form-control'}))
    gender_choice=(
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ')
    )
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={'class':'form-control'}))
    profile_pic = forms.FileField(label="Profile picture", widget=forms.FileInput(attrs={'class':'form-control'}))

class EditStudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=250, widget=forms.TextInput(attrs={'class':'form-control'}))
    khoas = Khoa.objects.all()
    khoa_list = []
    for khoa in khoas:
        khoa_list.append((khoa.id, khoa.tenkhoa))
    department = forms.ChoiceField(label="Department", choices=khoa_list, widget=forms.Select(attrs={'class':'form-control'}))
    gender_choice=(
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ')
    )
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={'class':'form-control'}))
    profile_pic = forms.FileField(label="Profile picture", widget=forms.FileInput(attrs={'class':'form-control'}), required=False)