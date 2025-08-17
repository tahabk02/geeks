# Exercise 1: Convert lists into dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)

# Exercise 2: Cinemax 
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name} has to pay ${price}")
    total_cost += price

print(f"Total family cost: ${total_cost}")

family = {}
while True:
    name = input("Enter family member name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

# Exercise 3: Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}
}

brand["number_stores"] = 2

print(f"Zara's clients are: {brand['type_of_clothes']}")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

print(brand.keys())

more_on_zara = {"creation_date": 1975, "number_stores": 10000}

brand.update(more_on_zara)

print(brand["number_stores"])

# Exercise 5: Random Number Comparison
import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success! Numbers match.")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

num = int(input("Enter a number between 1 and 100: "))
compare_numbers(num)

# Exercise 6: Personalized Shirts
def make_shirt(size="Large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'")

make_shirt()                     
make_shirt("Medium")               
make_shirt("Small", "Hello World")
make_shirt(text="Python Rocks", size="XL") 

# Exercise 7: Temperature Advice
import random

def get_random_temp(season=None):
    if season == "winter":
        lower, upper = -10, 16
    elif season == "spring":
        lower, upper = 0, 23
    elif season == "summer":
        lower, upper = 16, 40
    elif season == "autumn":
        lower, upper = 0, 32
    else:
        lower, upper = -10, 40
    return round(random.uniform(lower, upper), 1) 

def main():
    month = int(input("Enter month number (1-12): "))
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3,4,5]:
        season = "spring"
    elif month in [6,7,8]:
        season = "summer"
    else:
        season = "autumn"

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp}°C")

    if temp < 0:
        print("Brrr, that's freezing! Wear extra layers today")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 < temp <= 23:
        print("Mild weather today")
    elif 23 < temp <= 32:
        print("Warm outside, enjoy the sun!")
    else:
        print("Hot! Stay hydrated!")

main()

# Exercise 8: Star Wars Quiz
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def quiz():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for q in data:
        user_ans = input(q["question"] + " ")
        if user_ans.strip().lower() == q["answer"].lower():
            print("Correct!")
            correct += 1
        else:
            print("Incorrect!")
            incorrect += 1
            wrong_answers.append({"question": q["question"], "your_answer": user_ans, "correct_answer": q["answer"]})

    print(f"Correct: {correct}, Incorrect: {incorrect}")

    if wrong_answers:
        print("Review wrong answers:")
        for item in wrong_answers:
            print(f"Q: {item['question']}")
            print(f"Your answer: {item['your_answer']}, Correct: {item['correct_answer']}\n")

    if incorrect > 3:
        print("You had more than 3 wrong answers, try again!")
        quiz()

quiz()
