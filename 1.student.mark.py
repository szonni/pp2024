students = []
courses = []

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
    course_id = input("ID: ")
    course_name = input("Name: ")
    print('\n')
    return({"ID": course_id, "Name": course_name})


num_students = Number_Of_Students()           # Get the input number of students
for _ in range(num_students):
    stundent_info = Student_Infomation()
    students.append(stundent_info)            # Add student into students[]

num_courses = Number_Of_Courses()             # Get the input number of courses
for _ in range(num_courses):
    courses_info = Course_Information()
    courses.append(courses_info)              # Add course into courses[]