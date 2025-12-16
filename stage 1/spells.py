from classes import chrams
class Spells(chrams.Chrams):
    def __init__(self, spell_name, spell_effect):
        super().__init__(spell_name, spell_effect)
        self.spell_name = spell_name
        self.spell_effect = spell_effect
    def cast_spell(self):
        print(f"Casting {self.spell_name}: {self.spell_effect}")
        class Patronus(Spells):
            def __init__(self):
                super().__init__("Patronus Charm", "Conjures a protective Patronus")
            def cast_patronus(self):
                print("Expecto Patronum!")
                print("A shimmering Patronus appears, warding off Dementors!")
        class Levitation(Spells):
            def __init__(self):
                super().__init__("Levitation Charm", "Causes objects to levitate")
            def cast_levitation(self):
                print("Wingardium Leviosa!")
                print("The object rises into the air, floating gracefully!")
            class Disarming(Spells):
                def __init__(self):
                    super().__init__("Disarming Charm", "Disarms an opponent")
                def cast_disarming(self):
                    print("Expelliarmus!")
                    print("The opponent's wand flies out of their hand!")