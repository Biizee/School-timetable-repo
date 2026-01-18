import django_setup

from timetable.models import Teacher, Subject, Student, Class


#!--Creating teacher and subject
#first_teacher = Teacher.objects.create(
#    name = "Степан",
#
#)

#first_subject = Subject.objects.create(
#    name = "Математика",
#    teacher = first_teacher,
#
#)

#!--Getting first teacher and subject by their id
first_teacher = Teacher.objects.get(id = 1)
first_subject = Subject.objects.get(id = 1)

#!--Printing first teacher and subject
print(first_teacher)
print(first_subject)

#!--Printing related Teacher to Subject
print(first_subject.teacher)

#!--Creating student and his class
#first_class = Class.objects.create(
#    name = "1А",
#
#)
#
#first_student = Student.objects.create(
#    name = "Андрій",
#    student_class = first_class,
#
#)

#!--Getting student and class by their id
first_class = Class.objects.get(id = 1)
first_student = Student.objects.get(id = 1)

#!--Printing info about class and student
print(first_class)
print(first_student)

#!--Printing related Class to Student
print(first_student.student_class)
