import json
import math
import random
from storage import save_students,load_students

students = load_students()
       
            
while True:
  print("=" * 40)
  print("        STUDENT MANAGMENT SYSTEM")
  print("=" * 40)


  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Update Student")
  print("5. Delete Student")
  print("6. Add Marks")
  print("7. Add atendence")
  print("8. Exit")

  choice=input("enter your choice:")
  if choice == "1":
    Name = input("Enter student name: ")
    
    if Name.strip() == "":
        print("the name of the student cannot be empty")
        continue
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Please enter roll number as a number.")
        continue
    
    duplicate = False
    
    for student in students:
        if student[2] == roll:
            duplicate = True
            break
        
    if duplicate:
        print("student with this roll number already exists in the portal.")
        continue
    
    
    branch = input("Enter branch: ")
    
    if branch.strip()== "":
        print("BRANCH CANNOT BE EMPTY .")
        continue
    try:
        semester = int(input("Enter semester: "))
    except ValueError:
        print("Please enter semester as a number.")
        continue
    
    if semester < 1 or semester > 8:
        print("Entered semester must between 1 and 8 ")
        continue
    
    
    student_id = random.randint(1000, 9999)
    
    students.append([student_id, Name, roll, branch, semester])
    save_students(students)
    print("Student successfully added !")
    print("Student ID:",  student_id)
    

  elif choice == "2":
      if len(students) == 0:
        print("no students found. ")
      else: 
         print("student records: ")
         for student in students: 
            print(student)
    
  elif choice == "3":
      roll = input("enter roll number to search: ")
      
      found = False
      
      for student in students:
            if student[1] == roll:
                  print("student found!")
                  print("Student ID:", student[0])
                  print("Name:", student[1])
                  print("Roll Number:", student[2])
                  print("Branch:", student[3])
                  print("Semester:", student[4])
                  found = True
                  break
                
      if found == False:
                      print("Student not found.")
                      
  elif choice == "4":
    roll = input("Enter Roll number to update: ")
    found = False

    for student in students:
        if student[2] == roll:
            print("Student found !")
            
            student[1] = input("Enter the new name: ")
            student[3] = input("Enter new Branch : ")
            student[4] = input("Enter new Semester: ")
            
            save_students(students)
            print("Student updated successfully!")
            found = True
            break

    if found == False:
        print("Student not found.")                  
   
          
    

    
  elif choice == "5":
    roll = input("Enter the roll number to delete: ")
    found = False

    for student in students:
        if student[2] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully !")
            found = True
            break

    if found == False:
        print("Student not found.")
    elif choice == "6":
        roll = input("Enter roll number : ")
    found = False
    
    for student in students:
        if student[2] == roll:
            
            try:
                marks = float(input("Enter marks : "))
            except ValueError:
                print("Please enter marks as a number.")
                continue

            marks = math.floor(marks * 100) / 100

            if marks >= 90:
                grade = "A +"
            elif marks >= 80:
                grade = "B"
            elif marks >= 70:
                grade = "C"
            elif marks >= 60:
                grade = "D"
            else:
                grade = "F"

            student.append(marks)
            student.append(grade)
            save_students(students)

            print("Marks added successfully !")
            print("Grade:", grade)
            found = True
            break

    if found == False:
        print("Student not found .")   
        
 
    elif choice == "7":
        roll = input("Please enter the Roll number : ")
    found = False

    for student in students:
        if student[2] == roll:

            try:
                attendence = float(input("Please enter the attendence percentage : "))
            except ValueError:
                print("Please enter attendance as a number.")
                continue

            if attendence < 0 or attendence > 100:
                print("Attendance must be between 0 and 100.")
                continue

            student.append(attendence)
            save_students(students)

            print("Attendence added successfully!")
            print("Attendence : ", attendence, "%")

            found = True
            break

    if found == False:
        print("Student not found in the portal")
                            
  elif choice == "8":
    print("Thank you for using student portal ")
    break
                           
                    
