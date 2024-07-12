# 1.Avengers is a Marvel’s American Superheroes team, Now you want to
# showcase your programming skills by representing the Avengers team using
# classes. Create a class called Avenger and create these six superheroes using this
# class.
# 2. super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk",
# "Thor", "Hawkeye"]
# 3. Your Avenger class should have these properties:
# 1. Name
# 2. Age
# 3. Gender
# 4. Super Power
# 5. Weapon
# 4. Captain America has Super strength, Iron Man has Technology, Black Widow
# is superhuman, Hulk has Unlimited Strength, Thor has super Energy and
# Hawkeye has fighting skills as superpowers.
# 5. Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and
# Arrows
# 6. Create methods to get the information about each superhero
# 7. Create a method is_leader() which will tell if the superhero is a leader or not.


# Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    # method to get information about this heros
    def get_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Super Power: ", self.super_power)
        print("Weapon: ", self.weapon)

    # method to check if the superhero is a leader or not
    def is_leader(self):
        if self.name == "Captain America":
           return "Yes"
        else:
            return "No"

# Instances of Avenger Super heros
captain_america = Avenger("Captain America", 45, "Male", "Super Strength", "Shield")

iron_man = Avenger("Iron Man", 45, "Male", "Technology", "Armor")

black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")

hulk = Avenger("Hulk", 45, "Male", "Unlimited Strength", "Mjölnir")

thor = Avenger("Thor", 45, "Male", "Super Energy", "Bow")

hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")

# using method to get information and leadership
captain_america.get_info()
print("is Captain American the leader of Superheros: ", captain_america.is_leader())

iron_man.get_info()
print("is Iron Man the leader of Superheros: ", iron_man.is_leader())

black_widow.get_info()
print("is Black Widow the leader of Superheros: ", black_widow.is_leader())

hulk.get_info()
print("is Hulk the leader of Superheros: ", hulk.is_leader())

thor.get_info()
print("is Thor the leader of Superheros: ", thor.is_leader())

hawkeye.get_info()
print("is Hawkeye the leader of Superheros: ", hawkeye.is_leader())
