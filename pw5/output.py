def GPA(stdscr, students):
    stdscr.clear()
    for i, student in enumerate(students):
        gpa = student.cal_GPA()
        stdscr.addstr(i, 0, f"GPA for student ID {student.get_id()}: {gpa}")
        stdscr.refresh()

def sort_GPA(students):
    return sorted(students, key=lambda student: student.get_GPA(), reverse = True)