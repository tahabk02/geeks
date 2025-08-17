# Exercise 1 : Geometry
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius
    def perimeter(self):
       return 2 * math.pi * self.radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def definition(self):
         print("a circle is a srt of all points in a plan that are at a fixed distance (radius) from a center point.")

c1 = Circle(5)

print("Radius:", c1.radius)
print("Perimeter:", c1.perimeter())
print("Area:", c1.area())
c1.definition()

# Exercise 2 : Custom List Class

import random

class MyList:
    def __init__(self, letters):
        self.letters = letters
    def reversed_list(self):
        return self.letters[::-1]
    def sorted_list(self):
        return sorted(self.letters)
    def random_list(self):
        return [random.randint(0, 100) for _ in range(len(self.letters))]


if __name__ == "__main__":
    mylist = MyList(["b", "a", "d", "c", "e"])

    print("Original list:", mylist.letters)
    print("Reversed list:", mylist.reversed_list())
    print("Sorted list:", mylist.sorted_list())
    print("Random list:", mylist.random_list())
 
 
 # Exercise 3 : Restaurant Menu Manager   
     # menu_manager.py

class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

    def add_item(self, name, price, spice, gluten):
        self.menu.append({
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        })
        print(f"'{name}' added to the menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"'{name}' has been updated.")
                return
        print(f"Dish '{name}' is not in the menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f"'{name}' has been removed from the menu.")
                print("Updated menu:")
                for item in self.menu:
                    print(item)
                return
        print(f"Dish '{name}' is not in the menu.")

if __name__ == "__main__":
    manager = MenuManager()
    
    manager.add_item("Pizza", 20, "A", True)

    manager.update_item("Salad", 19, "B", False)
 
    manager.remove_item("Hamburger")
