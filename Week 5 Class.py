"""
AUthor: Muluk Muktar
Program:Class ""OOP"
Date: 3 - Oct-2025
"""
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}. My power is {self.power}.")

    def save_the_day(self):
        print(f"{self.name} uses {self.power} to save the day!")

# Inheritance Example
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} flies at {self.flight_speed} km/h!")

class StrongSuperhero(Superhero):
    def __init__(self, name, power, origin, strength_level):
        super().__init__(name, power, origin)
        self.strength_level = strength_level

    def lift(self):
        print(f"{self.name} lifts {self.strength_level} tons!")

# Usage
hero1 = FlyingSuperhero("Skyhawk", "Flight", "Cloud City", 300)
hero2 = StrongSuperhero("Titan", "Super Strength", "Earth", 100)

hero1.introduce()
hero1.fly()
hero2.introduce()
hero2.lift()
