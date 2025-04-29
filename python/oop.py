# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name}, and I got my powers from {self.origin}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass 1
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} mph using {self.power}!")

# Subclass 2
class StrengthHero(Superhero):
    def __init__(self, name, power, origin, lift_capacity):
        super().__init__(name, power, origin)
        self.lift_capacity = lift_capacity

    def use_power(self):
        print(f"{self.name} lifts {self.lift_capacity} tons with {self.power}!")

# == Example Usage ==
# hero1 = FlyingHero("Skyhawk", "Flight", "a mystical amulet", 500)
# hero2 = StrengthHero("Ironfist", "Super Strength", "gamma radiation", 100)

# hero1.introduce()
# hero1.use_power()

# hero2.introduce()
# hero2.use_power()


# === polymorphism ===
# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# == Example Usage ==
# vehicles = [Car(), Plane(), Boat()]

# for v in vehicles:
#     v.move()
