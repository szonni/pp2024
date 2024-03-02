import curses
import zipfile
import pickle
import os
from input import *
from output import *

def save_data(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_data(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def main(stdscr):
    # Decompression
    dat_file = "pw6/Info.dat"
    output = "pw6"
    if os.path.exists(dat_file):
        with zipfile.ZipFile(dat_file, "r") as zip_ref:
            zip_ref.extractall(output)

    # Main
    curses.curs_set(1)
    courses = load_data("pw6/students.pickle") or []
    students = load_data("pw6/courses.pickle") or []
    
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

    save_data("pw6/students.pickle", students)
    save_data("pw6/courses.pickle", courses)

    files = ["pw6/students.pickle", "pw6/courses.pickle"]
    output_data = "pw6/Info.dat"

    with zipfile.ZipFile(output_data, "w") as zip:
        for file in files:
            zip.write(file, os.path.basename(file))
    for file in files:
        os.remove(file)

# Program start
if __name__ == '__main__':
    curses.wrapper(main)