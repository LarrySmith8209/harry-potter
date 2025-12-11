import random
from school import school
from houses import house
from housecup import house_points
class houses:
    def __init__(self):
        self.houses = house.houses
class standings:
    def display_standings(self):
        sorted_scores = sorted(house_points.items(), key=lambda item: item[1], reverse=True)
        print("\n--- House Cup Standings ---")
        for rank, (house, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {house}: {score} points")
standings = standings()
standings.display_standings()
print(house_points)



class gethouse_points:
      for house, points in house_points.items():
          print(f"{house}: {points} points")
          def get_points(self, house_name):
              return house_points.get(house_name, 0)
            
              class tie_breaker:
                  def tie_qustion(self):
                   return "Tie breaker question"
          tie_breaker = tie_breaker()
          tie_breaker.tie_qustion=random.choice(house_points)
          playersinput= input("Enter the names of the players involved in the tie") 
          print("the winner of the tie breaker is and therefore the house cup winner is with a final points score of") (house_points+ random.points) ("is") (house) 
              

