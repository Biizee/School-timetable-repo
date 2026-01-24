from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField(unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_of_science = models.IntegerField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    day = models.IntegerField()
    start_time = models.TimeField()
    to_subj = models.ForeignKey(Subject, on_delete=models.PROTECT)
    to_class = models.ForeignKey(Class, on_delete=models.PROTECT)
    to_teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)

    def __str__(self):
        return self.to_subj, self.to_class, self.to_teacher
    
class Grade(models.Model):
    grade = models.IntegerField()
    date = models.DateField()
    to_student = models.ForeignKey(Student, on_delete=models.PROTECT)
    to_subj = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return self.to_student, self.to_subj
