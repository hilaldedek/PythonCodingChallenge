# 1. Python: Reverse Words and Swap Cases
# Implement a function that takes a string consisting of words separated by single spaces and returns a string containing all those words but in the reverse order and such that all cases of letters in the original string are swapped, i.e. lowercase letters become uppercase and uppercase letters become lowercase.
# Example
# sentence = "rUns dOg"
# Reverse the word order and swap the case of all letters, then return the string "DoG RuNS".

sentence = "rUns dOg"
result = ""
split_sent = sentence.split()
split_sent.reverse()
for i in range(len(split_sent)):
    for j in range(len(split_sent[i])):
        word = split_sent[i]
        if (ord(word[j]) >= 65 and ord(word[j]) <= 90):
            result += word[j].lower()
        elif (ord(word[j]) >= 97 and ord(word[j]) <= 122):
            result += word[j].upper()
    result += " "
print(result)
