# Write a Python function to check if a number is perfect.
# A perfect number is one that is half the sum of all its positive divisors (including itself). Example: The first perfect number is 6 because 1, 2, and 3 are proper positive divisors, and 1 + 2 + 3 = 6
number = int(input("please enter a number: "))
sum = 1
for i in range(2, (number//2)+1):
    if (number % i == 0):
        sum += i
if (sum == number):
    print("perfect number")
else:
    print("!perfect number")
