from domains.Student import Student
from domains.Course import Course
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
            student.enter_mark(stdscr, course_id)
        break
    curses.noecho()