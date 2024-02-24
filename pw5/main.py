import curses
import zipfile
import os
from input import input_student, input_course, mark
from output import GPA, sort_GPA

def main(stdscr):
    # Decompression
    dat_file = "pw5/students.dat"
    output = "pw5"
    if os.path.exists(dat_file):
        with zipfile.ZipFile(dat_file, "r") as zip_ref:
            zip_ref.extractall(output)

    # Main
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

    # Compress into .dat
    files = ["pw5/students.txt", "pw5/courses.txt", "pw5/marks.txt"]
    output_dat = "pw5/students.dat"

    with zipfile.ZipFile(output_dat, "w") as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    for file in files:
        os.remove(file)


# Program start
if __name__ == '__main__':
    curses.wrapper(main)