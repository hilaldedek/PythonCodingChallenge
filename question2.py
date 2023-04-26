# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
print("...Dizi için 5 eleman alınacaktır...")
array = []
minimum = 0
maximum = 0
for i in range(5):
    sayi = int(input(str(i) + ". eleman: "))
    array.append(sayi)
array.sort()
for i in range(4):
    minimum += array[i]
array.reverse()
for i in range(4):
    maximum += array[i]
