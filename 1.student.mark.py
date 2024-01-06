# Create lists and a dict for later usage
students = []
courses = []
marks = {}

def Number_Of_Students():
    return int(input("Number of students in class: "))

def Student_Infomation():
    student_id = input("ID: ")
    student_name = input("Name: ")
    Dob = input("Date Of Birth: ")
    print('\n')
    
    return({"ID": student_id, "Name": student_name, "DoB": Dob})

def Number_Of_Courses():
    return int(input("Number of courses: "))

def Course_Information():
    course_id = input("\nID: ")
    course_name = input("Name: ")
    
    return({"ID": course_id, "Name": course_name})

def Input_Mark():
    student_id = input("Enter student id: ")
    for student in students:
        if student_id != student['ID']:
            return print("Invalid student ID.")
    course_id =  input("Enter course id: ")
    for course in courses:
        if course_id != course['ID']:
            return print("Invalid course ID.")
    mark = float(input(f"\nEnter the mark for student id {student_id} in {course_id}: "))
    marks[(student_id, course_id)] = mark

def List_Marks():
    course_id =  input("Enter course id: ")
    for course in courses:
        if course_id != course['ID']:
            return print("Invalid course ID.")
    for list in students:
        student_id = list['ID']
        student_name = list['Name']
        student_DOB = list['DoB']
        if (student_id, course_id) in marks:
            print(f"ID: {student_id} | Name: {student_name} | Mark: {marks[(student_id, course_id)]} | DOB: {student_DOB} ")

def List_Course():
    for list in courses:
        print(f"ID: {list['ID']}; Name: {list['Name']}")

def List_Student():
    for list in students:
        print(f"ID: {list['ID']}; Name: {list['Name']}; DoB: {list['DoB']}")



#                   MAIN PROGRAM BEGINS                   #
for _ in range(Number_Of_Students()):
    students.append(Student_Infomation())            # Add student into students[]

for _ in range(Number_Of_Courses()):
    courses.append(Course_Information())              # Add course into courses[]

print('\n')
Input_Mark()
print('\n')
List_Student()
print('\n')
List_Course()
print('\n')
List_Marks()

#                   MAIN PROGRAM ENDS                    #

