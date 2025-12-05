from school import house
from sorting import quiz
from years import years
class player_creation:
    def create_player(self, name, age):
        self.name = name
        self.age = age
        print(f"Welcome {self.name}, age {self.age}, to the School of Magic!")
        # Sorting the player into a house
        sorted_house = quiz.sort
        self.house = sorted_house.storting(self, name)
        print(f"{self.name} has been sorted into {self.house} house!")
        # Assigning the player to the first year by default
        self.year = years.year1
        print(f"{self.name} is now a {self.year}.")
player = player_creation()
player.create_player("name", 11)
player.age= 11
for age in range(11,19):
    if player.age==age:
        print(f"Player age set to {player.age}")
        age+=1