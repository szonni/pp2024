import curses
from input import input_student, input_course, mark
from output import GPA, sort_GPA

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