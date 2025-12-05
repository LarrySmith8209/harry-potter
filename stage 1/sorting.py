import random 
from houses import house

class quiz:
  

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
    sorting= random.choice(house.houses)
    def get_sorting(self):
        return self.sorting