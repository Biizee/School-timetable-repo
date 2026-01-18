import django_setup

from timetable.models import Teacher, Subject


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
print(first_subject.name)
print(first_teacher.name)
