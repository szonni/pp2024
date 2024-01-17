from Classes.Student import Student
from Classes.Course import Course

def inputs(students):
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
        print("\n")
        courses.append(Course(id, name))   

def mark(students, courses):
    course_id = input("Enter course ID: ")
    if not any(course_id in course.get_id() for course in courses):
        print("Invalid course ID.")
        return
    for student in students:
        student.enter_mark(course_id)

     
# Main Function
def main():
    courses = []
    students = []
    inputs(students)
    input_course(courses)
    mark(students, courses)

    # List students' infomation
    print(students)
    # List courses' information
    print(courses)

# Starting Point
if __name__ == '__main__':
    main()