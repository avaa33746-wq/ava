# Create the initial list
foods = ["sushi", "strawberries", "hot chips", "hotpot", "chicken"]

# 1. Print the second food (Index 1 is the second item)
print(foods[1])

# 2. Print the last food using negative indexing
print(foods[-1])

# 3. Add a new food to the end using .append()
foods.append("tacos")

# 4. Insert ”apple” at the start (Index 0)
foods.insert(0, "apple")

# 5. Remove the third item using del
del foods[2]
#accidentally removed the 4 item by putting 3 in the brackects, I double checked my ode when i printed it and i realized i switched the order.

# 6. Print the length of the list
print(len(foods))
# i got this error cause i forgot my parenthesis  File "/Users/avaarreola/python_decal_fa25/ava/homework4/homework4.py", line 24
#    for food in foods:
#                    ^
#SyntaxError: invalid syntax

# 7. Loop through and print each food in uppercase
for food in foods:
    print(food.upper())

# 8. Create a new list with the first and last food using slicing
# [start:stop:step] - This takes the first item and the last
first_and_last = [foods[0], foods[-1]]
print(first_and_last)

# 9. If statement to check for "potato"
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

    # Create the initial list from 0 to 20 inclusive
numbers = list(range(21))

# 1. Function to get the first 15 elements
def get_first_15(nums):
    # Slicing from start to index 15
    return nums[:15]

# 2. Function to get every 5th element
def get_every_5th(lst):
    # Slicing with a step of 5
    return lst[::5]

# 3. Function to reverse and then take every 3rd
def reverse_and_stride(lst):
    # Step -1 reverses the list
    reversed_list = lst[::-1]
    # Return every 3rd element of that reversed list
    return reversed_list[::3]

# Putting it All Together
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

# Printing results to verify
print("Step 1 (First 15):", step1)
print("Step 2 (Every 5th):", step2)
print("Step 3 (Reverse & Stride):", step3)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Print the third row
print(numbers[2])

# 2. Print the second item in the second row
print(numbers[1][1])

# 3. Add [10, 11, 12] as a new row
numbers.append([10, 11, 12])

# 4. Function to sum all numbers in the nested list
def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        for num in row:
            total += num
    return total

# 1. Create a 5x5 list of numbers 1 to 25
def create_5x5():
    grid = []
    counter = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(counter)
            counter += 1
        grid.append(row)
    return grid

numbers_grid = create_5x5()

# 2. Replace multiples of 3 with "?"
def replace_multiples_of_3(input_grid):
    # Creating a deep copy to store in a new variable as requested
    new_grid = [row[:] for row in input_grid] 
    for r in range(len(new_grid)):
        for c in range(len(new_grid[r])):
            if new_grid[r][c] % 3 == 0:
                new_grid[r][c] = "?"
    return new_grid

updated_grid = replace_multiples_of_3(numbers_grid)

# 3. Sum all elements not equal to "?"
def sum_non_strings(input_grid):
    total = 0
    for row in input_grid:
        for item in row:
            if item != "?":
                total += item
    return total

final_sum = sum_non_strings(updated_grid)

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
#error SyntaxError: invalid syntax
#avaarreola@Avas-MacBook-Air homework4 % c
#avaarreola@Avas-MacBook-Air homework4 % /usr/bin/python3 /Users/avaarreola/python_decal_fa25/ava/homework4/homewor
#k4.py
#  File "/Users/avaarreola/python_decal_fa25/ava/homework4/homework4.py", line 142
#    print(ages["Katie"]), i forgot to last bracket

# 1. Print “Katie”’s age
print (ages["Katie"])
#another error avaarreola@Avas-MacBook-Air homework4 % /usr/bin/python3 /Users/avaarreola/python_decal_fa25/ava/homework4/homewor
#k4.py
#  File "/Users/avaarreola/python_decal_fa25/ava/homework4/homework4.py", line 147
#    print(ages["Katie"])
#    ^ the previous error made this an error too

# 2. Change Mira’s age to 100
ages["Mira"] = 100

# 3. Add "Milana" with an age of 52
ages["Milana"] = 52

# 4. Remove "Mariam" from the dictionary
del ages["Mariam"]

# 5. Use a for loop to print out each person’s name and age
for name, age in ages.items():
    print(f"{name}: {age}")

# --- Calling my favorite function ---
print("--- Grid with multiples of 3 replaced by '?' ---")
updated_grid_display = replace_multiples_of_3(numbers_grid)

# Printing row by row to make it look like a 5x5 square
for row in updated_grid_display:
    print(row)