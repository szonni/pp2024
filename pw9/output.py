import tkinter

def GPA(root, students, refresh):
    refresh(root)
    func_label = tkinter.Label(root, text="CALCULATED GPA", font=("Helvetica", 20))
    func_label.pack()
    
    for student in students:
        gpa = student.cal_GPA()

        gpa_label = tkinter.Label(root, text=f"GPA for student ID {student.get_id()}: {gpa}")
        gpa_label.pack()

def sort_GPA(students):
    return sorted(students, key=lambda student: student.get_GPA(), reverse = True)