from school import school
from playercreation import player
from years import year1, year2, year3, year4, year5, year6, year7
from classes import classes 
def main():
    print(f"Welcome to {school('canda School of Witchcraft and Wizardry').name}!")
    print(f"Student Name: {player.name}, Age: {player.age}, House: {player.house}")
    
    # Example of creating a first-year student
    first_year_student = year1(player.name, player.age)
    
    # Display class schedule for the first year
    first_year_schedule = classes.schedule(1)
    first_year_schedule.display_schedule()

if __name__ == "__main__":
    main()
    