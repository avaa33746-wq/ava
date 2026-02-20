# 3.1 Say Goodbye
def say_goodbye(name):
    print("Goodbye,", name)

# 3.2 Area of a Circle
def area_of_circle(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print("The area of the circle is:", area)
# 4.1 Subtract, Multiply and Divide
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Dividing a by b
    return a / b
# 5.1 What Should I Wear?
def get_temp_range(readings):
    # Find the smallest and largest numbers in the list
    lowest = min(readings)
    highest = max(readings)
    # Return them together as a tuple (low, high)
    return (lowest, highest)

# 5.2 Check if it’s the Weekend
def is_weekend(day_num):
    # Monday is 1, Friday is 5, Saturday is 6, Sunday is 7
    if day_num == 6 or day_num == 7:
        return True
    else:
        return False

#5.3 fuel efficiency
def fuel_efficiency(distance, fuel):
    """Calculates miles per gallon (MPG)."""
    return distance / fuel

#5.4 Secret Code
def encrypt_data(n):
    """Moves the last digit of an integer to the front."""
    if n < 10:
        return n
    
    last_digit = n % 10
    remaining_digits = n // 10
    
    # Calculate how many places to shift the last digit
    num_digits_remaining = len(str(remaining_digits))
    
    # Combine the parts: (last_digit * 10^power) + remaining_digits
    return (last_digit * (10 ** num_digits_remaining)) + remaining_digits

#6.1 
def manual_power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

#6.2 for loops
def find_min_for(nums):
    current_min = nums[0]
    for n in nums:
        if n < current_min:
            current_min = n
    return current_min

def find_max_for(nums):
    current_max = nums[0]
    for n in nums:
        if n > current_max:
            current_max = n
    return current_max

#6.2 while loops
def find_min_while(nums):
    current_min = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] < current_min:
            current_min = nums[i]
        i += 1
    return current_min

def find_max_while(nums):
    current_max = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] > current_max:
            current_max = nums[i]
        i += 1
    return current_max

#6.3 Calculate the sum
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # Add the last digit
        n //= 10         # Remove the last digit
    return total

# --- 4. Calling and Printing ---
# Calling 3.1 & 3.2 (These will print automatically when called)
say_goodbye("Oski")
area_of_circle(5)
# Let's use the manual_power function as the example
x = 2
y = 3
result = manual_power(x, y)

print(f"The result of Oski Stole Your Power (6.1) with x = {x} and y = {y} is {result}.")
