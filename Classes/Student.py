import math
import numpy
import curses

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__mark = {}
        self.__gpa = 0

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_GPA(self):
        return self.__gpa
    
    def enter_mark(self, stdscr, course_id):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, f"Enter the mark for student ID {self.__id}: ")
        mark = float(stdscr.getstr(1, 0).decode())
        mark = mark * 10
        mark = math.floor(mark)
        mark = mark / 10
        self.__mark[course_id] = numpy.array([mark])
        curses.noecho()

    def cal_GPA(self):
        course_score = 0
        course_num = 0
        for score in self.__mark.values():
            course_score += numpy.mean(score)
            course_num += 1
        self.__gpa = course_score / course_num
        return self.__gpa
    

    def __repr__(self):
        return f"ID: {self.__id}, Name: {self.__name}, DOB: {self.__dob}, Marks: {self.__mark}, {self.__gpa}"'\n'