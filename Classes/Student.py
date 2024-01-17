import math
import numpy

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__mark = {}
    
    def enter_mark(self, course_id):
        mark = float(input(f"Enter the mark for student ID {self.__id}: "))
        mark = mark * 10
        mark = math.floor(mark)
        mark = mark / 10
        self.__mark[course_id] = numpy.array([mark])
    
    def cal_GPA(self):
        course_score = 0
        course_num = 0
        for score in self.__mark.values():
            course_score += numpy.mean(score)
            course_num += 1
        gpa = course_score / course_num
        return gpa
    

    def __repr__(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DOB: {self.__dob}, Marks: {self.__mark}")
        print('\n')
        return

    