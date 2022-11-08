from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import StudentRegistration
from .models import User


# Create your views here.


def add_student(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
         name = fm.cleaned_data['name']
         email = fm.cleaned_data['email']
         password = fm.cleaned_data['password']
         user_registration = User(name=name, email=email, password=password)
         user_registration.save()
         fm = StudentRegistration

    else:
        fm = StudentRegistration
    student_data = User.objects.all()
    return render(request, 'add.html', {'form': fm, 'datas': student_data})


def update_student(request, id):
    if request.method == 'POST':
        user = User.objects.get(pk=id)
        student_form = StudentRegistration(request.POST, instance=user)
        if student_form.is_valid():
            user.save()
    else:
        user = User.objects.get(pk=id)
        student_form = StudentRegistration(instance=user)
    return render(request, 'updatestudent.html', {'form': student_form})


def delete_student(request, id):
    if request.method == 'POST':
      user = User.objects.get(pk=id)
      user.delete()
    return HttpResponseRedirect('/student/add')
