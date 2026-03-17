# 1. Git vs. GitHub: Git is the local software that tracks changes; 
#    GitHub is the online cloud platform where you host and share those tracked projects.

# 2. Terminal vs. Command Line: The "Command Line" is the actual interface where you 
#    type text commands; the "Terminal" is the environment/window that runs that interface.

# 3. Local vs. Remote Repository: Local is the version of the project living on your 
#    own computer; Remote is the version stored on a server (like GitHub).

# 4. Version Control: A system that records changes to files over time so you can 
#    recall specific versions later or collaborate without overwriting others' work.

# 5. Staging Area: A middle ground or "loading zone" where you gather specific 
#    changes you want to include in your next save (commit).

# 6. git add: Moves changes from your working directory to the Staging Area.

# 7. git commit: Takes everything in the Staging Area and saves it as a permanent 
#    snapshot (version) in your local history.

# 8. git push: Uploads your local commits to a remote repository (like GitHub).

# 9. git status: Shows the current state of your project—which files are changed, 
#    which are staged, and which are untracked.

# 10. git pull: Fetches updates from the remote repository and merges them 
#     into your local files.

# 11. pwd: "Print Working Directory"—shows you exactly which folder you are currently in.

# 12. ls: "List"—shows you all the files and folders inside your current directory.

# 13. cd: "Change Directory"—moves you from one folder to another.

# 14. nano: A simple, text-only editor that opens directly inside the terminal.

# 15. touch: Quickly creates a new, empty file.

# 16. mv: "Move"—used to move files to a new folder or rename them.

# 17. rm: "Remove"—permanently deletes a file (be careful, there is no trash bin!).

# 18. cat: "Concatenate"—quickly displays the entire contents of a file on your screen.

#3.2 A Directory Tree
# 1. To find your current working directory:
#pwd

# 2. To list all the files in your current working directory (~/python_decal/judy_decal):
#ls

# 3. To move to brianna_repo and pull the latest changes:
#cd ../brianna_repo
#git pull

# 4. To move the new homework.py to your personal homework/ folder:
# (Assuming you are currently inside brianna_repo)
#mv homework.py ../judy_decal/homework/

# 5. To move yourself (your terminal session) to that same directory:
#cd ../judy_decal/homework/

# 6. To view the contents of homework.py in your terminal:
#cat homework.py

# 7. To save changes and push from your local repository to your remote repository:
#git add .
#git commit -m "Finished homework"
#git push

# 8. Regarding the Git [rejected] error:
#
# Commands to resolve: 
# git pull 
# (Then, after resolving any conflicts)
# git push
#
# What the error means: The remote repository (on GitHub) contains changes that 
# you do not have on your local computer. This happens if someone else pushed 
# code to the same branch, or if Judy worked on a different computer and 
# pushed changes from there without updating her current machine first.

# 9. The absolute path that will allow you to move to Recent/:
#~/Recent/

#4.1 Data Types
def checkDataType(input_data):
    """Returns a string indicating the data type of the input."""
    return type(input_data).__name__

#4.2 Conditionals
def evenOrOdd(number):
    """Returns 'Even' if the integer is even, and 'Odd' otherwise."""
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
#5 Loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#6.1 Lists
def duplicateList(items):
    new_list = []
    for item in items:
        new_list.append(item)
        new_list.append(item)
    return new_list

#6.2 Debugging
#there is a missing colon, here is the fixed code:
def square(num):
    return num * num

# 7 running my code
def duplicateList(items):
    """
    Takes a list and returns a new list with each element duplicated.
    """
    new_list = []
    for item in items:
        new_list.append(item)
        new_list.append(item)
    return new_list

# Function call and print result
letters = ['a', 'b', 'c']
result = duplicateList(letters)
print(result)
