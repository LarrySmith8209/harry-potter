from school import school
from houses import house
from sorting import quiz
from classes import classes
import time

class year1:
    sudents = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        year1.sudents.append(self)
        year1sorted=quiz.sort
        self.house=year1sorted.storting(self,name)
        print(f"{self.name} has been sorted into {self.house}")
        for class_name in classes.year1_classes:
            print("class schedule", class_name,time)
            sort=quiz.sort

class year2:
    sudents = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        year2.sudents.append(self)
class year3:
    sudents = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        year3.sudents.append(self)
class year4:
    sudents = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        year4.sudents.append(self)
class year5:
    sudents = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        year5.sudents.append(self)
class year6:
    sudents = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        year6.sudents.append(self)
class year7:
    sudents = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        year7.sudents.append(self)
    def advance_year(self):
    

        years+= 1
        return years
        print(f"{self.name} has advanced to year {years}")
years = 1
def get_current_year():
    return years