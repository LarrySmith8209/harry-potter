from houses import house
from sorting import quiz
from housecup import housecup
from years import year1, year2, year3, year4, year5, year6, year7
from classes import classes
from semester import semester
from playercreation import player
from classes import schealdule

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
player_info_instance = player_info()
print(player_info_instance.get_player_info())
class school_events:
    def welcome_ceremony(self):
        return "Welcome Ceremony is held at the start of the school year to greet new students."
    
    def holiday_break(self):
        return "Holiday Break occurs in December, allowing students to return home for the holidays."
    
    def exams_period(self):
        return "Exams Period takes place at the end of each semester to assess student knowledge."
    

    class graduation_ceremony:       
        def ceremony_details(self):
        
           return "Graduation Ceremony is held at the end of the seventh year to celebrate student achievements."
    class house_cup_wins:
        house_wins = {
                              "phoehix": 7, 
                              "thunderbird": 4,
                              "dragon": 6,
                              "wolf": 6,
                              "hippogriff": 3,
                              "sphinx": 0
                        }
                        
    class quidditch_titles:
        titles = {
                              "phoehix": 5,
                              "thunderbird": 5,
                              "dragon": 4,
                              "wolf": 3,
                              "hippogriff": 0,
                              "sphinx": 0
                        }
        
    class quidditch_finals_history:
            finals_history= {
                "phoehix":["2016 champions","2020: Champions", "2021: Runners-up", "2022: Champions"],
                "thunderbird":["2019: Champions", "2020: Semi-finalists", "2021: Champions"],
                "dragon":["2018: Runners-up", "2019: Semi-finalists", "2020: Champions"],
                "wolf":["2017: Champions", "2018: Runners-up", "2019: Semi-finalists"],
                "hippogriff":["No appearances in finals"],
                "sphinx":["No appearances in finals"]
            }