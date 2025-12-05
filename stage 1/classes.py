import random  
from school import school
from years import year1, year2, year3, year4, year5, year6, year7
import time
class classes:
    year1_classes = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts level 1", "Charms", "Flying"]
    year2_classes = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts level 2", "Charms", "Care of Magical Creatures"]
    year3_classes = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts level 3 ", "Charms", "Divination", "History of Magic"]
    year4_classes = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts level 4", "Charms", "Care of Magical Creatures", "Arithmancy", "Muggle Studies"]
    year5_classes = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts level 5", "Charms", "Divination", "Ancient Runes", "Magical Law"]
    year6_classes = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts level 6", "Charms", "Care of Magical Creatures", "Advanced Potion-Making", "Dark Arts Defense"]
    year7_classes = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts level 7", "Charms", "Divination", "Magical Theory", "Wizarding History"]

    class schedule:
        def __init__(self, year):
            self.year = year
            if year == 1:
                self.classes = classes.year1_classes
            elif year == 2:
                self.classes = classes.year2_classes
            elif year == 3:
                self.classes = classes.year3_classes
            elif year == 4:
                self.classes = classes.year4_classes
            elif year == 5:
                self.classes = classes.year5_classes
            elif year == 6:
                self.classes = classes.year6_classes
            elif year == 7:
                self.classes = classes.year7_classes
            else:
                self.classes = []
        
        def display_schedule(self):
            print(f"Class schedule for Year {self.year}:")
            for class_name in self.classes:
                print(f"- {class_name} at {time.strftime('%H:%M:%S')}")
            return self.classes
        class times:
             def __init__(self, class_name, time):
                 self.class_name = class_name
                 self.time = time 
        def display_time(self):
                    print(f"{self.class_name} is scheduled at {self.time}")
                    return self.time