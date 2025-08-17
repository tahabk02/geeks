# Exercise 1: Birthday Look-up
birthdays = {
    "Taha": "2002/01/15",
    "Sara": "2000/06/20",
    "Adam": "1998/12/05",
    "Lina": "2001/03/10",
    "Youssef": "1999/09/30"
}
print("Welcome! You can look up the birthdays of the people in the list!")
name = input("Enter the person's name: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

# Exercise 2: Birthdays Advanced
print("Here are the people in the list:")
for person in birthdays.keys():
    print(person)

name = input("Enter the person's name: ")

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")

# Exercise 3: 
def sum_sequence(X):
    X_str = str(X)
    total = int(X_str) + int(X_str*2) + int(X_str*3) + int(X_str*4)
    return total

print(sum_sequence(3))  

# Exercise 4: Double Dice Simulation
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:
            break
    return count

def main():
    results = []
    for _ in range(100): 
        throws_needed = throw_until_doubles()
        results.append(throws_needed)
    
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()
