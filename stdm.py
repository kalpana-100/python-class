#DictWriter= creates list of dictionary

import csv 
def read_students(filename):
    students=[]
    with open(filename,'r')as file:
        reader=csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

def write_students(filename,students):
    with open(filename,'a',newline='')as file:
        fieldnames=['Name','Age','Class']
        writer=csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell()==0:
            writer.writeheader()
        for student in students:
            writer.writerow(student)

def ask_student_details():
    Name=input("Enter student name: ")
    Age=int(input("Enter student age: "))
    Class=input("Enter student class: ")
    return {'Name':Name,'Age':Age,'Class':Class}
write_students('students.csv',[ask_student_details()])

