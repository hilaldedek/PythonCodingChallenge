# Write a Python code to copy all of contents of dict1 to dict2 by doubling value numbers at below.

#    - Sample array:

#    ```python
#    dict1 = {'Apple': 15, 'Orange': 35, 'Melon': 20, 'Banana': 50, 'Pear': 40}
#    ```

#    - Expected Output :"Red, Green, White, Black"

#    ```python
#    dict2 = {'Apple': 30, 'Orange': 70, 'Melon': 40, 'Banana': 100, 'Pear': 80}
#    ```
dict1 = {'Apple': 15, 'Orange': 35, 'Melon': 20, 'Banana': 50, 'Pear': 40}
dict2 = {}
for k, v in dict1.items():
    dict2[k] = v * 2
print(dict2)
