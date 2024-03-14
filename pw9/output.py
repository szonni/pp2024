

def GPA(students):
    for student in students:
        student.cal_GPA()

def sort_GPA(students):
    return sorted(students, key=lambda student: student.get_GPA(), reverse = True)