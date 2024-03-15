import tkinter
import zipfile
import pickle
import os
import threading
from input import *
from output import *

def refresh(root):
    for widget in root.winfo_children():
        widget.destroy()

def save_data(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_data(filename):
    if not os.path.exists(filename):
        return None
    else:
        with open(filename, 'rb') as file:
            return pickle.load(file)

def main(root, students, courses):
    # Main    

    butt1 = tkinter.Button(root, text="Student", command=lambda: [refresh(root), input_student(root, students, courses, refresh, main)])
    butt1.pack()

    butt2 = tkinter.Button(root, text="Course", command=lambda: [refresh(root), input_course(root, students, courses, refresh, main)])
    butt2.pack()

    if len(students) == 0 or len(courses) == 0:
        butt3 = tkinter.Button(root, text="Mark", state="disabled")
        butt3.pack()
    else:
        butt3 = tkinter.Button(root, text="Mark", command=lambda: [refresh(root), mark(root, students, courses, refresh, main)])
        butt3.pack()

    GPA(students)
    
    # List students' infomation
    tkinter.Label(root, text="Students' Info", font=("Helvetica", 18)).pack()
    for i, student in enumerate(students, start = 1):
        tkinter.Label(root, text=f"{i}. ID: {student.get_id()} | Name: {student.get_name()} | DoB: {student.get_dob()} | Marks(course , mark): {student.get_marks()}", font=("Arial", 14)).pack(padx=5, pady=5)
    # List courses' information
    tkinter.Label(root, text="Courses' Info", font=("Helvetica", 18)).pack()
    for i, course in enumerate(courses, start = 1):
        tkinter.Label(root, text=f"{i}. ID: {course.get_id()} | Name: {course.get_name()}", font=("Arial", 14)).pack(padx=5, pady=5)

    sorted_students = sort_GPA(students)
    tkinter.Label(root, text="Sorted GPA", font=("Helvetica", 18)).pack(pady=10)
    
    for i, student in enumerate(sorted_students, start = 1):
        sorted_students_info = tkinter.Label(root, text=f"{i}. Name: {student.get_name()} | GPA: {student.get_GPA()}", font=("Arial", 14))
        sorted_students_info.pack(padx=5, pady=5)

    # Exit Button
    tkinter.Button(root, text="Exit", command=root.destroy).pack(pady=15)
    
    root.mainloop()

    save_thread1 = threading.Thread(target=save_data, args=("pw9/students.pickle", students))
    save_thread2 = threading.Thread(target=save_data, args=("pw9/courses.pickle", courses))
    
    save_thread1.start()
    save_thread2.start()
    
    save_thread1.join()
    save_thread2.join()

    files = ["pw9/students.pickle", "pw9/courses.pickle"]
    output_data = "pw9/Info.dat"

    with zipfile.ZipFile(output_data, "w") as zip:
        for file in files:
            zip.write(file, os.path.basename(file))
    for file in files:
        os.remove(file)

# Program start
if __name__ == '__main__':
        # Decompression
    dat_file = "pw9/Info.dat"
    output = "pw9"
    if os.path.exists(dat_file):
        with zipfile.ZipFile(dat_file, "r") as zip_ref:
            zip_ref.extractall(output)

    students = load_data("pw9/students.pickle") or []
    courses = load_data("pw9/courses.pickle") or []

    root = tkinter.Tk()
    root.geometry("800x600")
    root.title("Student Management System")
    
    main(root, students, courses)
