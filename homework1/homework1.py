#File: homework1 .py

# --- Variables and Data Types ---

# a = 10
a = 10         
print(a)
print(type(a)) 
# a is an integer, a whole number with no decimals

# b = 1.5
b = 1.5
print(b)
print(type(b)) 
# b is a float, a number with no decimal point

# c = 3j
c = 3j
print(c)
print(type(c)) 
# c is a complex number, a number withn a real and imaginary part

# d = "hello"
d = "hello"
print(d)
print(type(d)) 
# d is a string, a sequence of characters enclosed in quotes

# e = [1, 2, 3]
e = [1, 2, 3]
print(e)
print(type(e)) 
# e is a list, a collection of orded and changeable items allowing duplicates

# f = {"name": "Ellen", "favorite fruit": "strawberry"}
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) 
# f is a dictionary, a collection of key-value pairs that is unordered, changeable, and does not allow duplicate keys

# g = (1, 2)
g = (1, 2)
print(g)
print(type(g)) 
# g is a tuple, a collection which is ordered and unchangeable (immutable) items

# h = ["apple", "banana", "strawberry"]
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) 
# h is a list, a collection of ordered and changeable items

# i = True
i = True
print(i)
print(type(i)) 
# i is a boolean, a data type representing one of two values: True or False

# j = none
j = None
print(j)
print(type(j)) 
# j is a NoneType object, representing the absence of a value or a null value

# k += [True, "blue", 12]
k = [True, "blue", 12]
print(k)
print(type(k)) 
# k is a list, a collection of potentially different data types

# l = str(14)
l = str(14)
print(l)
print(type(l)) 
# l is a string, resulting from explicitly converting the integer 14 to a string

# m = 1e4
m = 1e4
print(m)
print(type(m)) 
# m is a float, representing 1 times 10 to the power of 4 (10000.0)
# --- End of variables and Data Types ---

# --- Comments ---
#1. How many different data types did you find? here are 9 distinct data types represented in the script.
#2. List all the data types you found. int, float, complex, str, list, dict, tuple, bool, NoneType
#3. What variables have the same data types? Same Types: floats: b and m and lists: e, h, and k
#4a. What was the data type of l? Data Type: l is a string (str).
#4b. Why is it not an integer? not an integer because it was wrapped in the str() function.
#4c.What does str() do? str() is a casting function that converts a value into its string (text) representation.
#5. Look up one more data type not given above. Repeat the same procedure. New Data Type (Set):

# n = {1, 2, 3}
n = {1, 2, 3}
print(n)
print(type(n))
# n is a set, an unordered collection of unique items.
# --- End of comments ---

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, non-empty strings are truthy
print(bool(123)) # True, non-zero numbers are truthy
print(bool([1, 2, 3])) # True, non-empty lists are truthy
print(bool(True)) # True, boolean True is truthy
print(bool(False)) # False, boolean False is falsy
print(bool(0)) # False, zero is falsy
print(bool("")) # False, empty strings are falsy
print(bool(" ")) # True, non-empty strings are truthy
print(bool(())) # False, empty tuples are falsy
print(bool([])) # False, empty lists are falsy
print(bool({})) # False, empty dictionaries are falsy
print(bool(True and False)) # False, both conditions need to be true
print(bool(True and True)) # True, both conditions are true
print(bool(False and False)) # False, both conditions are false
print(bool(True or False)) # True, at least one condition is true
print(bool(True or True)) # True, at least one condition is true
print(bool(False or False)) # False, both conditions are false
print(bool(not(False))) # True, negation of False is True
print(bool(not(True))) # False, negation of True is False

# --- comments ---
#What pattern do you notice about expressions returning True or False? I noticed that expressions returning True often involve non-empty values or conditions that evaluate positively, while those returning False typically involve empty values or conditions that evaluate negatively.
#Which expression surprised you about its result? The expressions that surprised me the most are the one with grouping symbols because i didnt know they can be false or true based on how they are grouped.
#Create an expression, not given above, that will return True. Why is it True? An expression that will return true is 100 != 50 because the != operator means "not equal to." Since 100 is indeed different from 50, the statement is mathematically True.
#Create an expression, not given above, that will return False. Why is it False? is 50 + 50 == 200 because the sum of 50 and 50 equals 100, which is not equal to 200, making the statement mathematically False.
# --- End of comments ---

#--- arithmetic operaters---
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division (always returns a float in Python)
print(5 % 2) # 1, % is the modulo operator (returns the remainder)
print(3 ** 2) # 9, ** performs exponentiation (3 to the power of 2)
print(15 // 2) # 7, // is floor division (rounds down to the nearest whole number) 
#--- end of arithmetic operaters---

#--- comparison operators---
print(5 == 2) # False, == checks if values are equal
print(10 != 10) # False, != checks if values are not equal
print(2 < 5) # True, < checks if the left is less than the right
print(12 > 5) # True, > checks if the left is greater than the right
print(5 <= 6) # True, <= checks if the left is less than or equal to the right
print(1 >= 10) # False, >= checks if the left is greater than or equal to the right
#--- end of comparison operators---

#--- assignments operators---
x=5 # assigns the value 5 to the variable x
x += 5 # 10, adds 5 to x and updates the variable (addition assignment)
x -= 4 # 1, subtracts 4 from x and updates the variable (subtraction assignment)
x *= 3 # 15, multiplies x by 3 and updates the variable (multiplication assignment) 
#--- end of assignments operators---

# 1. and: Returns True if both operands are true
#print(10 > 5 and 2 < 4)  # True, because both comparisons are true
#print(10 > 5 and 2 > 4)  # False, because the second comparison is false

#2. or: Returns True if at least one operand is true
#print(5 == 5 or 1 == 2)  # True, because the first part is true
#print(5 == 2 or 1 == 2)  # False, because both parts are false

# 3. not: Reverses the result (True becomes False, and vice versa)
#print(not 5 > 10)        # True, because 5 > 10 is False, and not(False) is True
#print(not 5 < 10)        # False, because 5 < 10 is True, and not(True) is False

#---More Questions:---
#1. What is the difference between / and //? 
# The / operator performs floating-point division, meaning it always returns a decimal (float), even if the numbers divide evenly. The // operator performs floor division, which returns only the whole number part of the quotient (rounding down to the nearest integer) and discards the remainder. 
#print(5 / 2) # 2.5
#print(5 // 2) # 2 
#2. What is the difference between % and //? While // (floor division) gives you the quotient (how many times a number fits), the % operator (modulo) gives you the remainder left over after that division. 
#print(10 // 3) # 3 (3 fits into 10 three times)
#print(10 % 3) # 1 (the remainder left over) 
#3. What operator would you use to calculate the remainder when dividing two numbers? Give an example. To calculate the remainder, use the modulo operator (%). 
#Example: print(17 % 5) # 2, because 5 goes into 17 three times with 2 left over. 
#4. How do assignment operators work?
#Simple Assignment (=): Stores the value on the right into the variable on the left (e.g., x = 10).
#Augmented Assignment (+=, -=, etc.): These are shorthands that perform a calculation on the variable's current value and then update it with the new result. For example, x += 5 is exactly the same as writing x = x + 5. 

my_string = "hello"
print(my_string) # hello, prints the entire string
print(my_string[0]) # h, accesses the character at the first position (index 0)
print(my_string[1]) # e, accesses the character at the second position
print(my_string[2]) # l, accesses the character at the third position
print(my_string[3]) # l, accesses the character at the fourth position
print(my_string[4]) # o, accesses the character at the fifth position
print(my_string[-1]) # o, uses negative indexing to get the last character
print(my_string[1:3]) # el, slices from index 1 up to (but not including) index 3
print(my_string[0:5:2]) # hlo, slices from index 0 to 5 with a step of 2 (skips every other letter)
print(len(my_string)) # 5, returns the total number of characters in the string
print(my_string + "goodbye") # hellogoodbye, concatenates (adds) the two strings together
print(my_string * 7) # hellohellohellohellohellohellohello, repeats the string 7 times

#3.4.1 Questions:
#1. Define the term slicing. For which of the manipulations did you slice your string? Slicing is a technique used to extract a specific portion (a "substring") of a string by specifying a starting index, an ending index, and an optional step. I used slicing in Manipulation 8 (my_string[1:3]) and Manipulation 9 (my_string[0:5:2]).
#2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)
#Result: Hello, my name is Oski
#Description: This uses the print() function to output multiple arguments. By default, Python automatically inserts a space between items separated by a comma.
#3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
#Result: Hello, my name is Oski
#Description: This uses an f-string (formatted string literal). The curly braces {} allow Python to evaluate the variable name and "plug" its value directly into the string.
#4. What is the difference between the two last print statements?
#While the visual output is the same, the mechanism is different:
#The Comma Method: Passes two separate objects to the print() function. print() handles the formatting by adding a space between them.
#The f-string Method: Evaluates the variable inside the string before it is even printed. This is generally preferred in modern Python because it is more readable, allows you to perform math or logic inside the braces, and gives you much more control over how the final text looks.
#--- End of questions ---

#--- comands ---
#1. cd
#Definition: Changes the current working directory.
#How to use: Type cd followed by the name of the folder you want to enter.
#Example: cd Documents
#2. ls
#Definition: Lists the files and folders in your current directory.
#How to use: Type ls and press enter.
#Example: ls
#3. ls -a
#Definition: Lists all files, including hidden ones (those starting with a dot .).
#How to use: Type ls followed by the -a (all) flag.
#Example: ls -a
#4. mkdir
#Definition: Creates a new directory (folder).
#How to use: Type mkdir followed by the name you want for your new folder.
#Example: mkdir Homework_Folder
#5. cat
#Definition: Concatenates and displays the content of a file.
#How to use: Type cat followed by the filename to read its contents in the terminal.
#Example: cat notes.txt
#6. pwd
#Definition: Print Working Directory. Shows the full path of where you are currently located.
#How to use: Type pwd and press enter.
#Example: pwd
#7. cd ..
#Definition: Moves up one level in the directory tree (to the parent folder).
#How to use: Type cd followed by a space and two dots.
#Example: cd ..
#8. cd .
#Definition: Refers to the current directory.
#How to use: Usually used as a reference point for running scripts or moving files to "here."
#Example: cd . (Note: This won't actually move you anywhere, as you are already there!)
#9. cd ~
#Definition: Moves you directly to your Home directory (the main folder for your user).
#How to use: Type cd followed by the tilde symbol.
#Example: cd ~
#10. cp
#Definition: Copies a file or directory from one place to another.
#How to use: Type cp [source] [destination].
#Example: cp notes.txt notes_backup.txt
#11. mv
#Definition: Moves or renames a file or directory.
#How to use: Type mv [source] [destination].
#Example: mv old_name.txt new_name.txt
#12. rm
#Definition: Removes (deletes) a file. Caution: There is no "Trash Can" here; once it's gone, it's usually gone forever!
#How to use: Type rm followed by the filename.
#Example: rm temporary_file.txt
#13. clear
#Definition: Clears the terminal screen of all previous text.
#How to use: Type clear and press enter.
#Example: clear
#14. grep
#Definition: Searches for a specific pattern of text within files.
#How to use: Type grep "search_term" filename.
#Example: grep "Python" assignment.txt
#--- End of commands ---

#command questions
#1. Look up 3 other commands not present. Define and explain how to use them on the command line.
#command1)touch: Creates a new, empty file or updates the timestamp of an existing one.
#Usage: touch <filename>
#Example: touch notes.txt
#command2)echo: Displays a line of text or the value of a variable to the terminal.
#Usage: echo "<text>"
#Example: echo "Learning Python is fun"
#command3)man: Short for "manual." It opens the documentation for almost any other command so you can see all its options.
#Usage: man <command>
#Example: man ls (press q to exit the manual) 
#2. What is the difference between ls and ls -a?
#ls: Lists only the "visible" files and directories in your current folder.
#ls -a: Lists all files, including those that are hidden. The -a flag tells the computer "do not ignore entries starting with a dot". 
#3. What is a hidden file? a hidden file (also called a "dotfile") is any file or directory whose name begins with a period (e.g., .bashrc or .config). 
#Purpose: They are typically used to store configuration settings for your apps or the system.
#Visibility: They don't appear in regular file listings to keep your folders decluttered and to prevent you from accidentally deleting important settings. 
#4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
#-l (Long format): Used with ls to show extra details like file size, permissions, and the date it was last modified. Usage: ls -l
#-r (Recursive): Used with rm or cp to perform an action on a folder and everything inside of it. Usage: rm -r my_folder
#-h (Human-readable): Often used with ls -l to display file sizes in a way humans understand (like "2KB" or "1GB") instead of just bytes. Usage: ls -lh