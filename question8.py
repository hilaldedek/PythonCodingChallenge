
# 1. Write a Python code that counts how many vowels and constants a string has that a user entered.

#    - Example:

#    ```bash
#    text : Today is Saturday
#    Your text has 6 vowels and 9 constants
#    ```
string = str(input("please enter a something: "))
string = string.lower()
vowels_count = 0
constants_count = 0
special_character = 0
vowels = ('a', 'e', 'o', 'ö', 'u', 'ü', 'ı', 'i')
constants = ('z', 'y', 'v', 't', 'ş', 's', 'r', 'p', 'n', 'r',
             'm', 'l', 'k', 'h', 'j', 'ğ', 'g', 'd', 'ç', 'c', 'b')
for i in string:
    if vowels.count(i) == 1:
        vowels_count += 1
    elif constants.count(i) == 1:
        constants_count += 1
    else:
        special_character += 1
print("vowels: ", vowels_count)
print("constants: ", constants_count)
print("special characters: ", special_character)
