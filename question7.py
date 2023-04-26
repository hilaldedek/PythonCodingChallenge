# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
number = str(input("please enter a number: "))
if (int(number) < 10):
    print(number)
else:
    while (int(number) >= 10):
        sum = 0
        for i in number:
            sum += int(i)
        number = str(sum)
    print("result:", sum)
