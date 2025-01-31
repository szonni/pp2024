from domains.Student import Student
from domains.Course import Course
import tkinter

def input_student(root, students, courses, refresh, main):
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
                if iterator < num:
                    refresh(root)
                    add_student(num)
                else:
                    refresh(root)
                    main(root, students, courses)

            add_butt = tkinter.Button(root, text="Append", command=append_student)
            add_butt.pack()

    butt = tkinter.Button(root, text="Add Students", command=lambda: add_student(int(num_input.get())))
    butt.pack()

def input_course(root, students, courses, refresh, main):
    func_label = tkinter.Label(root, text="COURSES INPUT", font=("Helvetica",20))
    func_label.pack()
    
    num_label = tkinter.Label(root, text="Number of courses: ")
    num_label.pack(anchor="nw")

    num_input = tkinter.Entry(root)
    num_input.pack(anchor="nw")
    iterator = 0

    
    def add_course(num):
        nonlocal iterator
        if iterator < num:
            id_label = tkinter.Label(root, text=f"Course number {iterator+1} | ID: ")
            id_label.pack()
            id_input = tkinter.Entry(root)
            id_input.pack()

            name_label = tkinter.Label(root, text="Name: ")
            name_label.pack()
            name_input = tkinter.Entry(root)
            name_input.pack()

            def append_course():
                nonlocal iterator
                c_id = id_input.get()
                c_name = name_input.get()
                courses.append(Course(c_id, c_name))
                iterator += 1
                if iterator < num:
                    refresh(root)
                    add_course(num)
                else:
                    refresh(root)
                    main(root, students, courses)
            add_butt = tkinter.Button(root, text="Append", command=append_course)
            add_butt.pack()
    butt = tkinter.Button(root, text="Add Courses", command=lambda: add_course(int(num_input.get())))
    butt.pack()

def mark(root, students, courses, refresh, main):
    func_label = tkinter.Label(root, text="MARKS INPUT", font=("Helvetica", 20))
    func_label.pack()

    courseid_label = tkinter.Label(root, text="Enter course ID: ")
    courseid_label.pack(anchor="nw")
    courseid_input = tkinter.Entry(root)
    courseid_input.pack(anchor="nw")
    index = 0
    
    def input_mark():
        nonlocal index
        nonlocal courseid_input
        c_id = courseid_input.get()
        if not any(c_id == course.get_id() for course in courses):
            label1 = tkinter.Label(root, text="Invalid course ID.")
            label1.pack()
            label2 = tkinter.Label(root, text="Please enter the correct course's ID: ")
            label2.pack()
            courseid_input = tkinter.Entry(root)
            courseid_input.pack()
        else:
            if index >= len(students):
                refresh(root)
                main(root, students, courses)
            else:
                students[index].enter_mark(root, c_id)
                index += 1

    butt = tkinter.Button(root, text="Continue", command=input_mark)
    butt.pack()
