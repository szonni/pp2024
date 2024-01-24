from Classes.Student import Student
from Classes.Course import Course
import curses



def input_student(stdscr, students):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Number of students is: ")
    stdscr.refresh()
    num = int(stdscr.getstr(1, 0).decode())
    
    for i in range (num):
        stdscr.addstr(2, 0,f"Student number {i+1} | ID: ")
        stdscr.refresh()
        id = stdscr.getstr(3, 0).decode()

        stdscr.addstr(4, 0, "Name: ")
        stdscr.refresh()
        name = stdscr.getstr(5, 0).decode()

        stdscr.addstr(6, 0, "DOB: ")
        stdscr.refresh()
        dob = stdscr.getstr(7, 0).decode()

        students.append(Student(id, name, dob))
    curses.noecho()

def input_course(stdscr, courses):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Number of courses: ")
    stdscr.refresh()
    num = int(stdscr.getstr(1, 0).decode())
    for i in range (num):
        stdscr.addstr(2, 0, f"Course number {i+1} | ID: ")
        stdscr.refresh()
        id = stdscr.getstr(3, 0).decode()

        stdscr.addstr(4, 0, "Name: ")
        stdscr.refresh()
        name = stdscr.getstr(5, 0).decode()

        courses.append(Course(id, name))
    curses.noecho()

def mark(stdscr, students, courses):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "///Mark input///")
    stdscr.refresh()
    stdscr.addstr(1, 0, "Enter course ID: ")
    stdscr.refresh()
    course_id = str(stdscr.getstr(2, 0).decode())
    while True:    
        if not any(course_id == course.get_id() for course in courses):
            stdscr.addstr(3, 0, "Invalid course ID.")
            stdscr.refresh()
            stdscr.addstr(4, 0, "Please enter the correct course's ID: ")
            stdscr.refresh()
            course_id = str(stdscr.getstr(5, 0).decode())
            continue
        for student in students:
            student.enter_mark(course_id)
        break
    curses.noecho()

def GPA(stdscr, students):
    stdscr.clear()
    for i, student in enumerate(students):
        gpa = student.cal_GPA()
        stdscr.addstr(i, 0, f"GPA for student ID {student.get_id()}: {gpa}")
        stdscr.refresh()

def sort_GPA(students):
    return sorted(students, key=lambda student: student.get_GPA(), reverse = True)
        
# Main Function
def main(stdscr):
    curses.curs_set(1)
    courses = []
    students = []
    
    input_student(stdscr, students)
    input_course(stdscr, courses)
    mark(stdscr, students, courses)

    GPA(stdscr, students)
    # List students' infomation
    stdscr.addstr(len(students) + 2, 0, str(students))
    stdscr.refresh()
    # List courses' information
    stdscr.addstr(len(courses) + 4, 0, str(courses))
    stdscr.refresh()

    sorted_students = sort_GPA(students)
    
    stdscr.addstr(len(students) + len(courses) + 6, 0, "///Sorting GPA in Descending order.///")
    stdscr.refresh()

    for i, student in enumerate(sorted_students):
        stdscr.addstr(i + len(students) + len(courses) + 8, 0, f"Name: {student.get_name()} | GPA: {student.get_GPA()}")
        stdscr.refresh()
    
    stdscr.getch()



# Program start
if __name__ == '__main__':
    curses.wrapper(main)