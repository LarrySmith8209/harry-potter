import random
from houses import house 
from  standings import standings   

# Initialize scores using a dictionary
house_points = {
    "phoehix": 0,
    "thunderbird": 0,
    "dragon": 0,
    "wolf": 0
}

def update_score(house_name, points):
    """Increments or decrements the score of a specific house."""
    if house_name in house_points:
        house_points[house_name] += points
        action = "gained" if points > 0 else "lost"
        print(f"{house_name} has {action} {abs(points)} points.")
    else:
        print(f"Error: {house_name} is not a valid house.")

def display_scores():
    """Prints the current scores for all houses, sorted from highest to lowest."""
    print("\n--- Current House Scores ---")
    # Sort the dictionary items by score in descending order
    sorted_scores = sorted(house_points.items(), key=lambda item: item[1], reverse=True)
    for house, score in sorted_scores:
        print(f"{house}: {score}")


update_score("phoehix",())
update_score={"thunderbird",()}
update_score("dragon",{})
update_score("wolf",{})

display_scores()
print(house_points)

class housecup:
    def winner(self):
        highest_score = max(house_points.values())
        winners = [house for house, score in house_points.items() if score == highest_score]
        if len(winners) == 1:
            return f"The winner of the House Cup is {winners[0]} with {highest_score} points!"
        else:
            return f"It's a tie between {' and '.join(winners)} with {highest_score} points each!"
        if tie in winners:
            return "It's a tie! A special competition will be held to determine the ultimate winner!"
house_cup = housecup()
print(house_cup.standings())

print(house_cup.winner())
class standings:
    def display_standings(self):
        sorted_scores = sorted(house_points.items(), key=lambda item: item[1], reverse=True)
        print("\n--- House Cup Standings ---")
        for rank, (house, score) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {house}: {score} points")
standings = standings()
standings.display_standings()
print(house_points)
