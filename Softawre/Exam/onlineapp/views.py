from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView

from .forms import UserRegisterForm
from .forms import StudentForm,TeacherForm
from .models import Student,Teacher
from django.contrib.auth.decorators import login_required

class Home(TemplateView):
    template_name = 'home.html'

"""@login_required
def dashboardView(request):
    return render (request,'dashboard.html')"""

def t_dashboardView(request):
    return render (request,'t_dashboard.html')

def s_dashboardView(request):
    return render (request,'s_dashboard.html')


@login_required
def selectView(request):
    return render (request,'select.html')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            ##messages.success(request, f'Your account has been successfully created!Log in now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def student_list(request):
    student = Student.objects.all()
    return render(request, 'student_list.html', {
        'student': student
    })

@login_required
def teacher_list(request):
    teacher = Teacher.objects.all()
    return render(request, 'teacher_list.html', {
        'teacher': teacher
    })


@login_required
def upload_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'upload_student.html', {
        'form': form
    })

@login_required
def upload_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'upload_teacher.html', {
        'form': form
    })


@login_required
def delete_student(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)

        student.delete()
    return redirect('student_list')

@login_required
def delete_teacher(request, pk):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=pk)

        teacher.delete()
    return redirect('teacher_list')


@login_required
def edit_student(request, pk) :
    student = Student.objects.get(pk=pk)
    return render(request,"edit_student.html", {'student': student})

@login_required
def edit_teacher(request, pk) :
    teacher = Teacher.objects.get(pk=pk)
    return render(request,"edit_teacher.html", {'teacher': teacher})


@login_required
def update_student(request, pk) :
    student =Student.objects.get(pk=pk)
    form = StudentForm(request.POST,request.FILES, instance= student)
    if form.is_valid():
        form.save()
        return redirect('/student/')
    return render(request,"edit_student.html", {'student': student})


@login_required
def update_teacher(request, pk) :
    teacher =Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST,request.FILES, instance= teacher)
    if form.is_valid():
        form.save()
        return redirect('/teacher/')
    return render(request,"edit_teacher.html", {'teacher': teacher})