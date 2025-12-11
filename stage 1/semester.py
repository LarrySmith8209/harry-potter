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