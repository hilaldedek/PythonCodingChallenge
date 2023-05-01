# Ask user to enter a word, a separator and number of repetitions. Write a Python code displaying the word with repetition times and having each word separated with separator character.

#    - For example, if user entered:

#       - word as Tina,
#       - separator as !
#       - repetitions as 3

#    - expected output:

#       "Tina!Tina!Tina"

#       Be careful there is no separator character at the end.
string = str(input("please enter a word: "))
seperator = str(input("please enter a seperator: "))
repeat = int(input("repeat number?: "))
word = []
result = ""
for i in range(repeat):
    word.append(string+seperator)
result = result.join(word)
sayi = (len(string)*int(repeat))+(repeat-1)
print(result[:int(sayi)])
