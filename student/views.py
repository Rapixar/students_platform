from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Department

def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student_show.html', {'student': student})            
# Create your views here.

def details(request, student_roll_no):
    student = Student.objects.get(roll_no=student_roll_no)
    details = str(student.name + '\n' + str(student.department) + '\n' + str(student.dateOfEnrol))
    return HttpResponse("The Student's details are as follows\n %s." % details)

def department(request, student_roll_no):
    student = Student.objects.get(roll_no=student_roll_no)
    department = student.department
    return HttpResponse("The student's department is %s." % department)

