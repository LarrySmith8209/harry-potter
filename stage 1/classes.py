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
             class semesters:
              semester1 = ["September", "October", "November", "December", "January"]
              semester2 = ["February", "March", "April", "May", "June"] 

              class exams:
                  midterms = ["Potions", "Herbology", "Transfiguration", "Defense Against the Dark Arts", "Charms"]
                  finals = ["Potions",  "Herbology", "Transfiguration", "Defense Against the Dark Arts", "Charms", "Care of Magical Creatures", "Divination", "History of Magic", "Arithmancy", "Muggle Studies", "Ancient Runes", "Magical Law", "Advanced Potion-Making", "Dark Arts Defense", "Magical Theory", "Wizarding History"]

                  class grading:
                      
                      def grade_student(student_name, class_name, score):
                          if score >= 90:
                              grade = 'A'
                          elif score >= 80:
                              grade = 'B'
                          elif score >= 70:
                              grade = 'C'
                          elif score >= 60:
                              grade = 'D'
                          else:
                              grade = 'F'
                          print(f"{student_name} received a grade of {grade} in {class_name}.")
                          return grade
                      
                          class attendance:
                              def record_attendance(student_name, class_name, present):
                               status = "present" if present else "absent"
                               print(f"{student_name} is {status} for {class_name}.")
                               return status
                          class schedule:
                            ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
                            def display_weekly_schedule(self):
                                print("Weekly Class Schedule:")
                                for day in self.schedule:
                                    print(f"- {day}")
                                return self.schedule
                            
                            class Potions:
                                def __init__(self):
                                    self.name = "Potions"
                                    self.time = "09:00 AM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Basic Potion-Making", "Advanced Potion-Making", "Healing Potions", "Poison Antidotes"]
                                    return self.topics
                            class Herbology:
                                def __init__(self):
                                    self.name = "Herbology"
                                    self.time = "11:00 AM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Magical Plants", "Plant Care", "Herbal Remedies", "Dangerous Flora"]
                                    return self.topics
                            class Transfiguration:
                                def __init__(self):
                                    self.name = "Transfiguration"
                                    self.time = "01:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Basic Transfiguration", "Human Transfiguration", "Animal Transfiguration", "Inanimate Objects"]
                                    return self.topics
                            class DefenseAgainsttheDarkArts:
                                def __init__(self):
                                    self.name = "Defense Against the Dark Arts"
                                    self.time = "03:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Dark Creatures", "Defensive Spells", "Counter-Curses", "Dark Arts History"]
                                    return self.topics
                            class Charms:
                                def __init__(self):
                                    self.name = "Charms"
                                    self.time = "04:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Basic Charms", "Charm Theory", "Advanced Charms", "Charm Applications"]
                                    return self.topics
                            class Flying:
                                def __init__(self):
                                    self.name = "Flying"
                                    self.time = "10:00 AM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Broomstick Basics", "Advanced Flying Techniques", "Flying Safety", "Quidditch Skills"]
                                    return self.topics
                            class CareOfMagicalCreatures:
                                def __init__(self):
                                    self.name = "Care of Magical Creatures"
                                    self.time = "02:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Magical Creature Care", "Creature Behavior", "Handling Techniques", "Creature Habitats"]
                                    return self.topics
                            class Divination:

                                def __init__(self):
                                    self.name = "Divination"
                                    self.time = "12:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Tea Leaf Reading", "Crystal Ball Gazing", "Astrology", "Dream Interpretation"]
                                    return self.topics
                            class HistoryOfMagic:
                                def __init__(self):
                                    self.name = "History of Magic"
                                    self.time = "11:00 AM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Magical History", "Famous Wizards", "Magical Wars", "Historical Events"]
                                    return self.topics
                            class Arithmancy:
                                def __init__(self):
                                    self.name = "Arithmancy"
                                    self.time = "01:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Numerology", "Magical Properties of Numbers", "Divination through Numbers", "Advanced Arithmancy"]
                                    return self.topics
                            class MuggleStudies:
                                def __init__(self):
                                    self.name = "Muggle Studies"
                                    self.time = "03:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Muggle Culture", "Muggle Technology", "Muggle History", "Muggle Society"]
                                    return self.topics
                            class AncientRunes:
                                def __init__(self):
                                    self.name = "Ancient Runes"
                                    self.time = "10:00 AM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Rune Translation", "Ancient Scripts", "Magical Inscriptions", "Rune History"]
                                    return self.topics
                            class MagicalLaw:
                                def __init__(self):
                                    self.name = "Magical Law"
                                    self.time = "12:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Wizarding Laws", "Legal Cases", "Magical Ethics", "Law Enforcement"]
                                    return self.topics
                            class AdvancedPotionMaking:
                                def __init__(self):
                                    self.name = "Advanced Potion-Making"
                                    self.time = "02:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Complex Potions", "Potion Ingredients", "Potion Effects", "Potion Safety"]
                                    return self.topics
                            class DarkArtsDefense:
                                def __init__(self):
                                    self.name = "Dark Arts Defense"
                                    self.time = "04:00 PM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Dark Arts Techniques", "Defensive Strategies", "Dark Creatures", "Counter-Dark Arts"]
                                    return self.topics
                            class MagicalTheory:
                                def __init__(self):
                                    self.name = "Magical Theory"
                                    self.time = "09:00 AM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Magic Fundamentals", "Spell Mechanics", "Magical Energy", "Theoretical Applications"]
                                    return self.topics
                            class WizardingHistory:
                                def __init__(self):
                                    self.name = "Wizarding History"
                                    self.time = "11:00 AM"
                                def display_info(self):
                                    print(f"Class: {self.name}, Time: {self.time}")
                                    self.topics = ["Wizarding Eras", "Famous Events", "Historical Figures", "Magical Societies"]
                                    return self.topics
                                