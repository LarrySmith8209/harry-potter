import random 
from houses import house

class quiz:
   for sorting in house.houses:
         print(f"Possible house: {sorting}")
         qustion=("how would pepole describe you? A: Brave B: Loyal C: Intelligent D: Ambitious E: Kind F: Mysterious")
         answer=input("Enter your answer (A-F): ")
print("You have answered the sorting question")
print("Sorting you into a house...")
print("You have been sorted! into"["house_name"])

class sort:
    def storting(self, name):
         for sorting in quiz.sorting:
             if sorting==house.houses[0]:
                 return f"{name} you are in phoehix"
             elif sorting==house.houses[1]:
                 return f"{name} you are in thunderbird"
             
             elif sorting==house.houses[2]:
                 return f"{name} you are in dragon"
             
             elif sorting==house.houses[3]:
                    return f"{name} you are in wolf"
             
             elif sorting==house.houses[4]:
                    return f"{name} you are in Hippogriff"
             elif sorting==house.houses[5]:
                    return f"{name} you are in sphinx"
    sorting= random.choice(house.houses)
    def get_sorting(self):
        return self.sorting
    def display_sorting(self):
        return f"The selected house is {self.sorting}"
    def invalid_answer(self, answer):
        if answer not in ['A', 'B', 'C', 'D', 'E', 'F']:
            return "Invalid answer. Please choose A, B, C, D, E, or F."
        
class final_sort:
    def final_sorting(self, name):
        sorter=sort()
        sorting=sorter.get_sorting()
        return sorter.storting(name)
    
    

        