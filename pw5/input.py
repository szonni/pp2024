from domains.Student import Student
from domains.Course import Course
import curses

def input_student(stdscr, students):
    curses.echo()
    f = open(r"pw5/students.txt", "w")          # Write to student.txt
    stdscr.clear()
    stdscr.addstr(0, 0, "Number of students is: ")
    stdscr.refresh()
    num = int(stdscr.getstr(1, 0).decode())
    f.write(f"Number of student is: {num}")
    
    for i in range (num):
        stdscr.addstr(2, 0,f"Student number {i+1} | ID: ")
        stdscr.refresh()
        id = stdscr.getstr(3, 0).decode()
        f.write(f"\nStudent number {i+1} | ID: {id}")

        stdscr.addstr(4, 0, "Name: ")
        stdscr.refresh()
        name = stdscr.getstr(5, 0).decode()
        f.write(f"\nName: {name}")

        stdscr.addstr(6, 0, "DOB: ")
        stdscr.refresh()
        dob = stdscr.getstr(7, 0).decode()
        f.write(f"\nDOB: {dob}")

        students.append(Student(id, name, dob))
    f.close()           # Close students.txt
    curses.noecho()

def input_course(stdscr, courses):
    curses.echo()
    f = open(r"pw5/courses.txt", "w")       # Write to courses.txt
    stdscr.clear()
    stdscr.addstr(0, 0, "Number of courses: ")
    stdscr.refresh()
    num = int(stdscr.getstr(1, 0).decode())
    f.write(f"Number of courses: {num}")
    
    for i in range (num):
        stdscr.addstr(2, 0, f"Course number {i+1} | ID: ")
        stdscr.refresh()
        id = stdscr.getstr(3, 0).decode()
        f.write(f"\nCourse number {i+1} | ID: {id}")

        stdscr.addstr(4, 0, "Name: ")
        stdscr.refresh()
        name = stdscr.getstr(5, 0).decode()
        f.write(f"\nName: {name}")

        courses.append(Course(id, name))
    f.close()          # Close courses.txt
    curses.noecho()

def mark(stdscr, students, courses):
    curses.echo()
    f = open(r"pw5/marks.txt", "w")              # Write to marks.txt
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
        f.write(f"\nCourse ID: {course_id}")
        for student in students:
            student.enter_mark(stdscr, course_id, f)
        break
    f.close()           # Close marks.txt
    curses.noecho()