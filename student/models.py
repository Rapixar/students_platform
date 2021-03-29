import datetime #Imports the datetime built-in utility

from django.utils import timezone #Imports the django timezone utility

from django.db import models #Imports the models paackage form Django base utlity

# Create your models here.
class Department(models.Model):   
    division = models.TextField() # A kind of categorixzation feature
    name = models.TextField(max_length=20)
    importance = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True, serialize=True)
    name = models.CharField(max_length=40)
    stud_class = models.CharField("Student's class", max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    dateOfEnrol = models.DateTimeField("Date of Enrolment")
    def __str__(self): # Gives a human readable name for referencing the object
        return self.name
    def enrolled_recently(self):
        return self.dateOfEnrol >= timezone.now() - datetime.timedelta(days=1)