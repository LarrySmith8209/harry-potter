from houses import house
from sorting import quiz
from housecup import housecup
from years import year1, year2, year3, year4, year5, year6, year7
from classes import classes
from semester import semester
from playercreation import player
class school:
    def __init__(self, name):
       self.name = name
       self.houses = house.houses
         
    class years:
        year1 = "First Year"
        year2 = "Second Year"
        year3 = "Third Year"
        year4 = "Fourth Year"
        year5 = "Fifth Year"
        year6 = "Sixth Year"
        year7 = "Seventh Year"
class player_info:
    def get_player_info(self):
        return f"Player Name: {player.name}, Age: {player.age}, House: {player.house}"