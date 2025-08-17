# Exercise 1: Hello World
print("Hello world\n" * 4)

# Exercise 2: Some Math
result = (99 ** 3) * 8
print(result)

# Exercise 3: What’s your name
my_name = "Taha"
user_name = input("What`s your name? ")

if user_name.lower() == my_name.lower():
    print("Wow! We have the same name ")
else:
    print(f"Nice to meet you, {user_name}!")

# Exercise 4: Tall enough to ride a roller coaster
height = int(input("Enter your height in cm: "))

if height > 145:
    print("You are tall enough to ride the roller coaster!")
else:
    print("You need to grow some more to ride.")

# Exercise 5: Favorite Numbers

my_fav_numbers = {3, 7, 21}


my_fav_numbers.add(42)
my_fav_numbers.add(99)

my_fav_numbers.pop()


friend_fav_numbers = {8, 13, 21}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 6: Tuple
my_tuple = (1, 2, 3)

my_tuple = my_tuple + (4,)
print(my_tuple)

# Exercise 7: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]


basket.remove("Banana")
basket.remove("Blueberries")


basket.append("Kiwi")           
basket.insert(0, "Apples")      


apple_count = basket.count("Apples")
print("Number of Apples:", apple_count)


basket.clear()
print(basket)
