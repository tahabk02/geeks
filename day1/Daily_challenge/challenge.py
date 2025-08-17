# Challenge 1: List of Multiples

number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

multiples = [number * i for i in range(1, length + 1)]

print(multiples)

# Challenge 2:

word = input("Enter a word: ")
new_word = word[0]   

for char in word[1:]:
    if char != new_word[-1]:  
        new_word += char

print(new_word)
