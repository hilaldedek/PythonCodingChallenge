# persistence Write a function that returns the multiplicative persistence of a positive parameter field number num, the number by which you must multiply the steps until it reaches a single digit.
# persistence(39) # returns 3, because 39=27, 27=14, 1*4=4 # and 4 has only one digit
# persistence(999) # returns 4, because 999=729, 729=126, # 126=12, and finally 1*2=2
# persistence(4) # returns 0, because 4 is already a one-digit number
counter = 0
number = str(input("please enter a number: "))

if (int(number)/10 < 1):
    print("0 step")
else:
    while (int(number) >= 10):
        result = 1
        for i in number:
            result *= int(i)
        counter += 1
        number = str(result)


print(counter, " step")
