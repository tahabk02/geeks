
# day3:
    
#  Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Luna", 3)
cat2 = Cat("Milo", 5)
cat3 = Cat("Simba", 2)


def get_oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)


oldest = get_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

#  Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")



davids_dog = Dog("Rex", 50)
print(f"David's dog name: {davids_dog.name}")
print(f"David's dog height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print()  


sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog name: {sarahs_dog.name}")
print(f"Sarah's dog height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

print() 

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}")
else:
    print("Both dogs are the same height.")


#  Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to {self.name}")
        else:
            print(f"{new_animal} is already in the zoo!")

    def get_animals(self):
        print(f"Animals in {self.name}:")
        for animal in self.animals:
            print(f"- {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.name}")
        else:
            print(f"{animal_sold} is not in the zoo!")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)
        
       
        for key in grouped:
            if len(grouped[key]) == 1:
                grouped[key] = grouped[key][0]
        self.grouped_animals = grouped

    def get_groups(self):
        if hasattr(self, 'grouped_animals'):
            print("Animal groups:")
            for letter, group in self.grouped_animals.items():
                print(f"{letter}: {group}")
        else:
            print("Please sort the animals first using sort_animals().")

new_york_zoo = Zoo("New York Zoo")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")
print()
new_york_zoo.get_animals()
print()
new_york_zoo.sell_animal("Bear")
print()
new_york_zoo.get_animals()
print()
new_york_zoo.sort_animals()
new_york_zoo.get_groups()
