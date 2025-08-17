# Exercise 1: What is the Season
month = int(input("Enter the month number (1-12)"))
if 3 <= month <= 5:
    print("Spring")
elif 6<= month <= 8:
    print("Summer")
elif 9<= month <= 11:
    print("Winter")
    
else:
    print("Invalid month number!")
    
# Exercise 2: For Loop
for i in range(1, 21):
    print(i)
for i in range(1, 21):
    if i % 2 == 0:   
        print(i)

# Exercise 3: While Loop

my_name = "Taha"
user_name = ""
while user_name != my_name:
    user_name = input("Enter your name: ")
print("Welcome Taha!")
# Exercise 4: Check the Index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
search_name = input("Enter a name to search: ")

if search_name in names:
    print(f"The first occurrence of {search_name} is at index {names.index(search_name)}")
else:
    print(f"{search_name} is not in the list.")

# Exercise 5: Greatest Number
num1 = float(input("Input the 1st number: "))
num2 = float(input("Input the 2nd number: "))
num3 = float(input("Input the 3rd number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

# Exercise 6: Random Number Game
import random

wins = 0
losses = 0

while True:
    user_input = input("Enter a number from 1 to 9 (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break

    user_number = int(user_input)
    random_number = random.randint(1, 9)

    if user_number == random_number:
        print("Winner ")
        wins += 1
    else:
        print(f"Better luck next time. The number was {random_number}")
        losses += 1

print(f"Total games won: {wins}")
print(f"Total games lost: {losses}")
