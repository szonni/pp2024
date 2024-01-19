from Classes.Student import Student
from Classes.Course import Course



def input_student(students):
    num = int(input("Number of students is: "))
    for _ in range (num):
        id = input("ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        print("\n")
        students.append(Student(id, name, dob))

def input_course(courses):
    num = int(input("Number of courses: "))
    for _ in range (num):
        id = input("ID: ")
        name = input("Name: ")
        courses.append(Course(id, name))   

def mark(students, courses):
    print("\n///Mark input///")
    course_id = str(input("Enter course ID: "))
    while True:    
        if not any(course_id == course.get_id() for course in courses):
            print("Invalid course ID.")
            course_id = str(input("Please enter the correct course's ID: "))
            continue
        for student in students:
            student.enter_mark(course_id)
        print('\n')
        break

def GPA(students):
    for student in students:
        gpa = student.cal_GPA()
        print(f"GPA for student ID {student.get_id()}: {gpa}")
    print('\n')

def sort_GPA(students):
    return sorted(students, key=lambda student: student._Student__gpa, reverse = True)
        
# Main Function
def main():
    courses = []
    students = []
    input_student(students)
    input_course(courses)
    mark(students, courses)

    GPA(students)
    # List students' infomation
    print(students)
    # List courses' information
    print(courses)
    sorted_students = sort_GPA(students)
    print("///Soring GPA in Descending order.///")
    for student in sorted_students:
        print(f"Name: {student.get_name()} | GPA: {student.get_GPA()}")

# Starting Point
if __name__ == '__main__':
    main()