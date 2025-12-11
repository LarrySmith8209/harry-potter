from school import school
from classes import classes
class quarter:
    def __init__(self, quarter_number):
        self.quarter_number = quarter_number
        print(f"Semester initialized: Quarter {self.quarter_number}")
    def display_quarter(self):
        return f"This is Quarter {self.quarter_number} of the semester."
    def advance_quarter(self):
        self.quarter_number += 1
        return self.quarter_number
    for quarter in range(1, 5):
        print(f"Quarter {quarter} is part of the semester.")
class semester:
    def __init__(self, semester_number):
        self.semester_number = semester_number
        self.quarters = [quarter(1), quarter(2)]
        print(f"Semester initialized: Semester {self.semester_number}")
    def display_semester(self):
        return f"This is Semester {self.semester_number}."
    def advance_semester(self):
        self.semester_number += 1
        return self.semester_number
    def get_quarters(self):
        return self.quarters
semester1 = semester(1)
semester2 = semester(2)
semester+=1

print(semester1.display_semester())
print(semester2.display_semester())
for q in semester1.get_quarters():
    print(q.display_quarter())
for q in semester2.get_quarters():
    print(q.display_quarter())
semester1.advance_semester()
print(f"Advanced to Semester {semester1.semester_number}")
semester2.advance_semester()
print(f"Advanced to Semester {semester2.semester_number}")

class classscheule:
    def __init__(self, semester):
        self.semester = semester
        self.classes = classes()
    def display_schedule(self):
        print(f"Class schedule for Semester")
        for class_name in self.classes.year1_classes:
            print(f"- {class_name}")
class_schedule_sem1 = classscheule(semester1)
class_schedule_sem2 = classscheule(semester2)
    
