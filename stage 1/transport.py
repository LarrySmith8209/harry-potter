import random
from transport import transport_options
class TransportQuiz:
    def __init__(self):
        self.transport = None

    def ask_question(self):
        print("Choose your preferred mode of transport:")
        question = ("A: Flying B: Swimming C: Driving D: Biking E: Walking F: Teleporting")
        answer = input("Enter your answer (A-F): ")
        print("You have answered the transport question")
        print("Selecting your transport option...")
        self.transport = random.choice(transport_options)

    def get_transport(self):
        return self.transport

    def display_transport(self):
        return f"The selected mode of transport is {self.transport}"
transport_quiz = TransportQuiz()
transport_quiz.ask_question()
print(transport_quiz.display_transport())
class transport_sort:
    def transport_choice(self, name):
         for option in transport_options:
             if option == transport_options[0]:
                 return f"{name}, you prefer Flying"
             elif option == transport_options[1]:
                 return f"{name}, you prefer Swimming"
             elif option == transport_options[2]:
                 return f"{name}, you prefer Driving"
             elif option == transport_options[3]:
                 return f"{name}, you prefer Biking"
             elif option == transport_options[4]:
                 return f"{name}, you prefer Walking"
             elif option == transport_options[5]:
                 return f"{name}, you prefer Teleporting"
    selected_transport = random.choice(transport_options)
    def get_selected_transport(self):
        return self.selected_transport
    def display_selected_transport(self):
        return f"The selected transport option is {self.selected_transport}"
transport_sort_instance = transport_sort()
print(transport_sort_instance.display_selected_transport())
