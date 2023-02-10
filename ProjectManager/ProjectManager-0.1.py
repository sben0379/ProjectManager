# Open user and tasks files as a+

f1 = open("user.txt", "r+")
f2 = open("tasks.txt", "r+")

# Read user.txt and append each line to logins list

logins = []

lines = f1.read().splitlines()
for line in lines:
    temp = line.split(", ")
    logins.append(temp)

# Ask user to enter username and password and combine to match logins list format. If username-password
# pair exists in logins, proceed to menu. Else print error message and ask again.

user_login = []
username = input("Please enter your username")
user_password = input("Please enter your password")

user_login.append(username)
user_login.append(user_password)

while user_login not in logins:
    print("Your username and/or password is not recognised. Please try again.")
    username = input("Please enter your username")
    user_password = input("Please enter your password")

while True:
    
    # Present the menu to the user and convert inputs to lower case.
    
    menu = input("""Select one of the following Options below:
r - Register a user
a - Add a task
va - View all tasks
vm - View my task
s - View statistics
e - Exit
: """).lower()

# Register: ask user to input new username, password and password confirmation. If password and 
# password confirmation match, write to user.txt. Else print error message and ask again.

    if menu == "r":
        if username == "admin":
            new_username = input("Please enter a new username")
            new_password = input("Please enter a new password")
            confirm_password = input("Please confirm your password")

            while new_password != confirm_password:
                print("Sorry, your passwords do not match. Please try again.")
                new_password = input("Please enter a new password")
                confirm_password = input("Please confirm your password")
        
            if new_password == confirm_password:
                with open("user.txt", "a+") as f_user:
                    f_user.write("\n" + str(new_username) + ", " + str(new_password))

        else:
            print("You are not authorised to perform this action")

# Add task: Ask user to input username of asignee, title and description of task, and the due date. Get
# current date and include 'No' to indicate task completion. Write to tasks.txt

    elif menu == "a":
        pass
        assignee = input("Please enter the username of the person whom the task is assigned to")
        task_title = input("Please enter a title for the task")
        task_description = input("Please enter a description of the task")
        due_date = input("Please enter the due date for the task (eg. 19 Dec 2022")
        from datetime import datetime
        now = datetime.now()
        date = now.strftime("%d %b %Y")
    
        with open("tasks.txt", "a+") as f_tasks:
            f_tasks.write("\n" + str(assignee) + ", " + str(task_title).title() + ", " + str(task_description).title() + ", " + str(date) + ", " + str(due_date) + ", No")
        
# View all: Display all data from tasks.txt in user-friendly format. Loop through each line and split at
# ", " then print.

    elif menu == "va":
        f2.seek(0)
        lines = f2.read().splitlines()
        print("All tasks: \n")
        for line in lines:
            temp = line.split(", ")
            print(
                "\nTask: \t\t\t" + str(temp[1]) +
                "\nAssigned to: \t\t" + str(temp[0]) +
                "\nDate assigned: \t\t" + str(temp[3]) +
                "\nDue date: \t\t" + str(temp[4]) +
                "\nTask complete? \t\t" + str(temp[5]) +
                "\nTask description: \t" + str(temp[2]) +
                "\n"
                )

# View my tasks: Display only tasks assigned to user. Loop through each line and split at ", ". If 
# assignee in tasks.txt matches username then print. 

    elif menu == "vm":
        f2.seek(0)
        lines = f2.readlines()
        print("My tasks: \n")
        for line in lines:
            temp = line.split(", ")
            if temp[0] == username:
                print(
                "\nTask: \t\t\t" + str(temp[1]) +
                "\nAssigned to: \t\t" + str(temp[0]) +
                "\nDate assigned: \t\t" + str(temp[3]) +
                "\nDue date: \t\t" + str(temp[4]) +
                "\nTask complete? \t\t" + str(temp[5]) +
                "\nTask description: \t" + str(temp[2]) +
                "\n"
                )
            else:
                continue

# If user is admin and selects s, print number of lines in tasks and user files 

    elif menu == "s":
        if username == "admin":
            f1.seek(0)
            lines = f1.read().splitlines()
            print("Number of users: " + str(len(lines)))
            f2.seek(0)
            lines = f2.read().splitlines()
            print("Number of tasks: " + str(len(lines)))
        else:
            print("You are not authorised to perform this action")

# Exit: print goodbye message then exit programme.
        
    elif menu == "e":
        print("Goodbye!")
        exit()

# If user enters any other input, print error message

    else:
        print("Error: invalid input. Please enter a command from the menu provided.")