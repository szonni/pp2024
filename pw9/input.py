from domains.Student import Student
from domains.Course import Course
import tkinter

def input_student(root, students, refresh):
    func_label = tkinter.Label(root, text="STUDENTS INPUT", font=("Helvetica",20))
    func_label.pack()
    
    num_label = tkinter.Label(root, text="Number of students is: ")
    num_label.pack(anchor="nw")
    
    num_input = tkinter.Entry(root)
    num_input.pack(anchor="nw")
    iterator = 0
    

    def add_student(num):
        nonlocal iterator
        if iterator < num:
            id_label = tkinter.Label(root, text=f"Student number {iterator+1} | ID: ")
            id_label.pack()
            id_input = tkinter.Entry(root)
            id_input.pack()

            name_label = tkinter.Label(root, text="Name: ")
            name_label.pack()
            name_input = tkinter.Entry(root)
            name_input.pack()

            dob_label = tkinter.Label(root, text="DOB: ")
            dob_label.pack()
            dob_input = tkinter.Entry(root)
            dob_input.pack()

            def append_student():
                nonlocal iterator
                s_id = id_input.get()
                s_name = name_input.get()
                s_dob = dob_input.get()
                students.append(Student(s_id, s_name, s_dob))
                iterator += 1
                refresh(root)
                add_student(num)

            add_butt = tkinter.Button(root, text="Append", command=append_student)
            add_butt.pack()

    butt = tkinter.Button(root, text="Add Students", command=lambda: add_student(int(num_input.get())))
    butt.pack()

def input_course(root, courses, refresh):
    refresh(root)
    func_label = tkinter.Label(root, text="COURSES INPUT", font=("Helvetica",20))
    func_label.pack()
    
    num_label = tkinter.Label(root, text="Number of courses: ")
    num_label.pack(anchor="nw")

    num_input = tkinter.Entry(root)
    num_input.pack(anchor="nw")

    
    def add_course():
        num = int(num_input.get())
        for i in range (num):
            id_label = tkinter.Label(root, text=f"Course number {i+1} | ID: ")
            id_label.pack()
            id_input = tkinter.Entry(root)
            id_input.pack()

            name_label = tkinter.Label(root, text="Name: ")
            name_label.pack()
            name_input = tkinter.Entry(root)
            name_input.pack()

            courses.append(Course(id_input.get(), name_input.get()))
    butt = tkinter.Button(root, text="Add Courses", command=lambda: [refresh(root), add_course()])
    butt.pack()

def mark(root, students, courses, refresh):
    refresh(root)
    func_label = tkinter.Label(root, text="MARKS INPUT", font=("Helvetica", 20))
    func_label.pack()

    courseid_label = tkinter.Label(root, text="Enter course ID: ")
    courseid_label.pack()
    courseid_input = tkinter.Entry(root)
    courseid_input.pack()
    
    while True:    
        if not any(courseid_input.get() == course.get_id() for course in courses):
            label1 = tkinter.Label(root, text="Invalid course ID.")
            label1.pack()

            label2 = tkinter.Label(root, text="Please enter the correct course's ID: ")
            label2.pack()
            courseid_input = tkinter.Entry(root)
            courseid_input.pack()
            continue
        for student in students:
            student.enter_mark(root, courseid_input.get())
        break
