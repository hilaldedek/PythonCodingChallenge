# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
import numpy as np
left = 0
right = 0
a = int(input("How many square matrices?: "))
my_array = np.array(range(a*a)).reshape(a, a)
for i in range(a):
    for j in range(a):
        my_array[i][j] = int(
            input(str(i)+"*"+str(j) + " what is the number?: "))
print("Entered matrix:\n", my_array)
for i in range(a):
    left += my_array[i][i]
j = 0
for i in range(a-1, -1, -1):
    right += my_array[j][i]
    j += 1
result = abs(right-left)

print("result:", result)
