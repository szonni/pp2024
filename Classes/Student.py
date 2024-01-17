class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__mark = {}

    def enter_mark(self, course_id):
        mark = float(input(f"Enter the mark for student {self.__id}: "))
        self.__mark[course_id] = mark

    def __repr__(self):
        return f"ID: {self.__id}, Name: {self.__name}, DOB: {self.__dob}, Marks: {self.__mark}\n"

    