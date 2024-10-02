from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student

# Create your views here.
def index(request):
    return render(request, 'students/index.html')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})
def student_add(request):
    students = Student.objects.all()
    return render(request, 'students/student_add.html', {'students': students})
def student_edit(request):
    students = Student.objects.all()
    return render(request, 'students/student_edit.html', {'students': students})