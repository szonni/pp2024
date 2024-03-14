import math
import numpy
import tkinter

def delete_previous_children(root):
    children = root.winfo_children()
    if len(children) >= 2:
        children[-1].destroy()  # Destroy the last child
        children[-2].destroy()  # Destroy the second last child

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__mark = {}
        self.__gpa = 0

    def get_id(self):
        return self.__id
    
    def get_dob(self):
        return self.__dob
    
    def get_name(self):
        return self.__name
    
    def get_GPA(self):
        return self.__gpa
    
    def get_marks(self):
        return self.__mark
    
    def enter_mark(self, root, course_id):
        mark_label = tkinter.Label(root, text=f"Enter the mark for student ID {self.__id}: ")
        mark_label.pack()
        mark_input = tkinter.Entry(root)
        mark_input.pack()

        def add_mark():
            mark = float(mark_input.get())
            mark = mark * 10
            mark = math.floor(mark)
            mark = mark / 10
            self.__mark[course_id] = mark
        comfirm = tkinter.Button(root, text="Confirm", command=lambda: [add_mark(), delete_previous_children(root)])
        comfirm.pack()

    def cal_GPA(self):
        course_score = 0
        course_num = 0
        for score in self.__mark.values():
            course_score += numpy.mean(score)
            course_num += 1
        self.__gpa = course_score / course_num
    

    def __repr__(self):
        return f"ID: {self.__id}, Name: {self.__name}, DOB: {self.__dob}, Marks: {self.__mark}, {self.__gpa};"'\n'