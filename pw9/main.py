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

def main():
    # Decompression
    dat_file = "pw9/Info.dat"
    output = "pw9"
    if os.path.exists(dat_file):
        with zipfile.ZipFile(dat_file, "r") as zip_ref:
            zip_ref.extractall(output)

    students = load_data("pw9/students.pickle") or []
    courses = load_data("pw9/courses.pickle") or []
    
    # Main    
    root = tkinter.Tk()
    root.geometry("800x600")
    root.title("Student Management System")



    butt1 = tkinter.Button(root, text="Student", command=lambda: [refresh(root), input_student(root, students, refresh)])
    butt1.pack()
    #input_course(root, courses, refresh)
    #mark(root, students, courses, refresh)
    
    #GPA(root, students, refresh)
    
    # List students' infomation
    students_info = tkinter.Label(root, text=str(students), font=("Arial", 18))
    students_info.pack(padx=30, pady=30)
    # List courses' information
    courses_info = tkinter.Label(root, text=str(courses), font=("Arial", 18))
    courses_info.pack(padx=30, pady=30)

    sorted_students = sort_GPA(students)
    
    for student in sorted_students:
        sorted_students_info = tkinter.Label(root, text=f"Name: {student.get_name()} | GPA: {student.get_GPA()}", font=("Arial", 18))
        sorted_students_info.pack(padx=30, pady=30)
    
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
    main()