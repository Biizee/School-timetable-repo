import django_setup

from timetable.models import Teacher, Subject, Student, Class, Schedule, Grade
from django.core.exceptions import ObjectDoesNotExist

def list_students_and_classes():
    classes = Class.objects.all()
    if classes:
        for clas in classes:
            print(f"\nClass id - {clas.id}. Class - {clas.name}. \nStudents:")
            students = Student.objects.filter(student_class_id = clas)
            if students:
                for student in students:
                    print(f"Student id - {student.id}. Name - {student.name}")

def list_subjects_and_teachers():
    teachers = Teacher.objects.all()
    if teachers:
        for teacher in teachers:
            print(f"\nTeacher id - {teacher.id}. Name - {teacher.name}")
            subjects = Subject.objects.filter(teacher_id = teacher)
            if subjects:
                for subject in subjects:    
                    print(f"Subject id - {subject.id}. Subject - {subject.name}. \n")

def create_class():
    name = input("Enter class name (for example: 3B): ")
    try:
        age = int(input("Enter age of science of class (for example: 3): "))
        clas = Class.objects.create(name = name, age_of_science = age)
    except Exception as e:
        print(f"\nError: {e}")
    print(f"Class {clas.name} created succesfully!")

def create_student():
    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    try:
        class_id = int(input("Enter class id: "))
        student = Student.objects.create(
            name = name,
            surname = surname,
            student_class_id = class_id
        )
        print(f"\nStudent was succesfully created!")
    except ObjectDoesNotExist:
        print(f"\nClass doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def create_teacher():
    name = input("Enter teacher name: ")
    surname = input("Enter teacher surname: ")
    teacher = Teacher.objects.create(name = name, surname = surname)
    print(f"Teacher {teacher.name} created succesfully!")

def create_subject():
    name = input("Enter subject name: ")
    desc = input("Enter subject description: ")
    try:
        teacher_id = int(input("Enter teacher id: "))
        subject = Subject.objects.create(
            name = name,
            desc = desc,
            teacher_id = teacher_id
        )
        print(f"\nSubject was succesfully created!")
    except ObjectDoesNotExist:
        print(f"\nTeacher doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")
    
def create_schedule():
    try:
        day = int(input("\nEnter number of the day (min 1, max 7): "))
        if day <= 7 and day > 0:
            time = input("\nEnter start time of lesson (for example: 17:59:59): ")
            to_subj = int(input("\nEnter subject id: "))
            to_subj = Subject.objects.get(id = to_subj)
            to_class = int(input("Enter class id: "))
            to_class = Class.objects.get(id = to_class)
            to_teacher = int(input("Enter teacher id: "))
            to_teacher = Teacher.objects.get(id = to_teacher)
            schedule = Schedule.objects.create(
                day = day,
                start_time = time,
                to_subj = to_subj,
                to_class = to_class,
                to_teacher = to_teacher
            )
            print(f"\nSchedule was succesfully created!")
        else:
            print("Wrong number, try again!")
    except ObjectDoesNotExist:
        print(f"\nTeacher or class or subject doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}") 
    
def create_grade():
    try:
        grade = int(input("\nEnter grade (min 1, max 12): "))
        if grade > 0 and grade <= 12:
            date = input("\nEnter date (for example: 2026-01-28): ")
            to_student = int(input("\nEnter student id: "))
            to_student = Student.objects.get(id = to_student)
            to_subj = int(input("Enter student id: "))
            to_subj = Subject.objects.get(id = to_subj)
            grade_obj = Grade.objects.create(
                grade = grade,
                date = date,
                to_student = to_student,
                to_subj = to_subj
            )
            print(f"\nGrade was succesfully created!")
        else:
            print("Wrong number, try again!")
    except ObjectDoesNotExist:
        print(f"\nStudent or subject doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}") 

def edit_class():
    try:
        clas = int(input("Enter class id: "))
        clas = Class.objects.get(id = clas)
        new_name = input("\nEnter new name for class (leave blank to keep current): ")
        if new_name:
            clas.name = new_name
        new_age = int(input("\nEnter age of science of class (leave blank to keep current): "))
        if new_name:
            clas.age_of_science = new_age
        clas.save()
        print("\nClass edited succesfully!")
    except ObjectDoesNotExist:
        print(f"\nClass doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def edit_student():
    try:
        student = int(input("Enter student id: "))
        student = Student.objects.get(id = student)
        new_name = input("\nEnter new name for student (leave blank to keep current): ")
        if new_name:
            student.name = new_name
        new_surname = input("\nEnter new surname for student (leave blank to keep current): ")
        if new_surname:
            student.surname = new_surname
        new_class = int(input("Enter new class id for student (leave blank to keep current): "))
        if new_class:
            clas = Class.objects.get(id = new_class)
            student.student_class_id = clas
        student.save()
        print("\nStudent edited succesfully!")
    except ObjectDoesNotExist:
        print(f"\nStudent or class doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def edit_teacher():
    try:
        teacher = int(input("Enter teacher id: "))
        teacher = Teacher.objects.get(id = teacher)
        new_name = input("\nEnter new name for teacher (leave blank to keep current): ")
        if new_name:
            teacher.name = new_name
        new_surname = input("\nEnter new surname for teacher (leave blank to keep current): ")
        if new_surname:
            teacher.surname = new_surname
        teacher.save()
        print("\nTeacher edited succesfully!")
    except ObjectDoesNotExist:
        print(f"\nTeacher doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def edit_subject():
    try:
        subject = int(input("Enter subject id: "))
        subject = Subject.objects.get(id = subject)
        new_name = input("\nEnter new name for subject (leave blank to keep current): ")
        if new_name:
            subject.name = new_name
        new_desc = input("\nEnter new description for subject (leave blank to keep current): ")
        if new_desc:
            subject.desc = new_desc
        new_teacher = int(input("Enter new teacher id for subject (leave blank to keep current): "))
        if new_teacher:
            teacher = Teacher.objects.get(id = new_teacher)
            subject.teacher_id = teacher
        subject.save()
        print("\nSubject edited succesfully!")
    except ObjectDoesNotExist:
        print(f"\nTeacher or subject doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_class():
    try:
        clas = int(input("Enter class id: "))
        clas = Class.objects.get(id = clas)
        clas.delete()
        print("\nClass deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nClass doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_student():
    try:
        stident = int(input("Enter student id: "))
        stident = Student.objects.get(id = stident)
        stident.delete()
        print("\nStudent deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nStudent doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_teacher():
    try:
        teacher = int(input("Enter teahcer id: "))
        teacher = Teacher.objects.get(id = teacher)
        teacher.delete()
        print("\nTeacher deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nTeacher doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_subject():
    try:
        subject = int(input("Enter subject id: "))
        subject = Subject.objects.get(id = subject)
        subject.delete()
        print("\nSubject deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nSubject doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

while True:
    print("""
Options:
1. List all students and classes
2. list all teachers and subjects
3. Create new class
4. Create new student
5. Create new teacher
6. Create new subject
7. Create new schedule
8. Create new grade
9. Edit class
10. Edit student
11. Edit teacher
12. Edit subject
13. Delete class
14. Delete student
15. Delete teacher
16. Delete subject
17. Exit""")
    
    try:
        choice = int(input("\nEnter your choice: "))
    except Exception as e:
        print(f"Error: {e}")
    
    if choice == 17:
        break

    elif choice == 1:
        list_students_and_classes()

    elif choice == 2:
        list_subjects_and_teachers()
    
    elif choice == 3:
        create_class()
    
    elif choice == 4:
        create_student()
    
    elif choice == 5:
        create_teacher()
    
    elif choice == 6:
        create_subject()
    
    elif choice == 7:
        create_schedule()
    
    elif choice == 8:
        create_grade()
    
    elif choice == 9:
        edit_class()
    
    elif choice == 10:
        edit_student()
    
    elif choice == 11:
        edit_teacher()
    
    elif choice == 12:
        edit_subject()
    
    elif choice == 13:
        delete_class()
    
    elif choice == 14:
        delete_student()
    
    elif choice == 15:
        delete_teacher()
    
    elif choice == 16:
        delete_subject()

    else:
        print("Invalid choice, try again!")

