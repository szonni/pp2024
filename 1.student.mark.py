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
    if not any(student_id in student['ID'] for student in students):
        print("Invalid student ID.")
        return
    course_id =  input("Enter course id: ")
    if not any(course_id in course['ID'] for course in courses):
        print("Invalid course ID.")
        return 
    mark = float(input(f"\nEnter the mark for student id {student_id} in {course_id}: "))
    marks[(student_id, course_id)] = mark

def List_Marks():
    course_id =  input("Enter course id: ")
    if not any(course_id in course['ID'] for course in courses):
        print("Invalid course ID.")
        return 
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

# Main Function
def main():    
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

#                   MAIN PROGRAM BEGINS                   #
if __name__ == '__main__':
    students = []
    courses = []
    marks = {}
    main()
#                   MAIN PROGRAM ENDS                    #


