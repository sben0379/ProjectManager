# Import data from text files and store in global lists. Import modules and create variable to track the 
# current user.

from datetime import datetime
import random
current_user = []
users = []
tasks = []



with open('user.txt', 'r') as f_users:
    lines = f_users.read().split(', ')
    for i in lines:
        users.append(i)

with open('tasks.txt', 'r') as f_tasks:
    lines = f_tasks.read().splitlines()
    for line in lines:
        temp = line.split(', ')
        tasks.append(temp)

# Define write functions to take file name and mode input and write to that file. Do not add comma to
# final index

def write_user(filename, mode):
    with open(str(filename), str(mode)) as file:
        count = 0
        new_string = ''
        for i in users:
            if count == len(users) - 1:
                new_string += str(i)
            else:
                new_string += str(i) + ', '
                count += 1
        file.seek(0)
        file.write(new_string)

def write_task(filename, mode):
    wiped_file = open('tasks.txt', 'w')
    wiped_file.close()
    with open(str(filename), str(mode)) as file:
        new_string = ''
        rows = len(tasks)
        for row in range(rows):
            cols = len(tasks[row])
            for col in range(cols):
                if tasks[row][col] == tasks[row][-1]:
                    new_string += str(tasks[row][col]) + '\n'
                else: 
                    new_string += str(tasks[row][col]) + ', '
            file.seek(0)
            file.write(new_string)
            new_string = ''

# Define login function to ask user to input username and password and check if exists in users variable

def login():
        while True:
            username_input = input("Please enter your username: ")
            password_input = input("Please enter your password: ")
            if username_input in users:
                password_index = users.index(username_input) + 1
                user_password = users[password_index]
                if password_input == user_password:
                    current_user.append(username_input)
                    print('\nWelcome back')
                    return False
                else:
                    print('Your username and/or password is not recognised. Please try again.')
            else:
                print('Your username and/or password is not recognised. Please try again.')

# Define register function to ask user to input new username, password and password confirmation. If 
# password and password confirmation match, write to user.txt. Else print error message and ask again. If 
# the new username already exists, print an error message and ask again. If the user is not admin, print 
# error message

def register():
    if current_user[0] == "admin":
        new_username = input("Please enter a new username: ")
        new_password = input("Please enter a new password: ")
        confirm_password = input("Please confirm your password: ")
        
        if new_username in users:
            while new_username in users:
                print("\nSorry, that username is already in use.")
                new_username = input("Please enter a new username: ")
                new_password = input("Please enter a new password: ")
                confirm_password = input("Please confirm your password: ")
        while new_password != confirm_password:
                print("\nSorry, your passwords do not match. Please try again.")
                new_password = input("Please enter a new password: ")
                confirm_password = input("Please confirm your password: ")

        if new_password == confirm_password:
            users.append(str(new_username))
            users.append(str(new_password))
            write_user('user.txt', 'w')
    else:
        print("\nYou are not authorised to perform this action")

# Define add task function to ask user to input a task ID, username of asignee, title and description of 
# task, and the due date. Get current date and include 'No' to indicate task completion. If task id already 
# exists in tasks.txt print error message and ask again. Write to tasks.txt

def add_task():
    task_number = random.randint(1, 100)
    for i in range(len(tasks)):
        if task_number == tasks[i][0]:
            while task_number == tasks[i][0]:
                task_number = random.randint(1, 100)
        else:
            continue
    assignee = input("Please enter the username of the person whom the task is assigned to: ")
    task_title = input("Please enter a title for the task: ")
    task_description = input("Please enter a description of the task: ")
    due_date = input("Please enter the due date for the task (eg. 19 Dec 2022): ")
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    
    new_row = str(task_number) + ', ' + str(assignee) + ', ' + str(task_title) + ', ' + str(task_description) + ', ' + str(date) + ', ' + str(due_date) + ', No'
    new_list = new_row.split(', ')
    tasks.append(new_list)

    write_task('tasks.txt', 'a+')

# Define view all function to display all data from tasks.txt in user-friendly format. Loop through each 
# outer list in tasks and print each index in inner loop

def view_all():
    print("\nAll tasks: \n")
    rows = len(tasks)
    for row in range(rows):
        print(
            "\nTask ID: \t\t" + str(tasks[row][0]) +
            "\nTask: \t\t\t" + str(tasks[row][2]) +
            "\nAssigned to: \t\t" + str(tasks[row][1]) +
            "\nDate assigned: \t\t" + str(tasks[row][4]) +
            "\nDue date: \t\t" + str(tasks[row][5]) +
            "\nTask complete? \t\t" + str(tasks[row][6]) +
            "\nTask description: \t" + str(tasks[row][3]) +
            "\n"
            )

# Define edit function to allow user to select task by its number ID and change either its completion status, 
# due date or assignee. Allow user to return to main menu by entering -1 

def task_edit():
    while True:
        user_input = input("Enter a task number to select a task or '-1' to return to the main menu: ")
        if user_input == "-1":
            return False
        else:
            rows = len(tasks)
            for row in range(rows):
                if tasks[row][0] == user_input:
                    print(
                    "\nTask ID: \t\t" + str(tasks[row][0]) +
                    "\nTask: \t\t\t" + str(tasks[row][2]) +
                    "\nAssigned to: \t\t" + str(tasks[row][1]) +
                    "\nDate assigned: \t\t" + str(tasks[row][4]) +
                    "\nDue date: \t\t" + str(tasks[row][5]) +
                    "\nTask complete? \t\t" + str(tasks[row][6]) +
                    "\nTask description: \t" + str(tasks[row][3]) +
                    "\n"
                    )
                    options = input("""\nSelect one of the following options: 
                    1 - Mark task as complete
                    2 - Edit task due date 
                    3 - Edit task assignee 
                    4 - Return to main menu 
                    """)        
                    if options == "1":
                        tasks[row][-1] = 'Yes'
                        write_task('tasks.txt', 'a+')
                        return False
                    elif options == "2":
                        date_input = input("Please enter a new due date: ")
                        tasks[row][-2] = date_input
                        write_task('tasks.txt', 'a+')
                        return False
                    elif options == "3":
                        assignee_input = input("Please enter a new assignee for this task: ")
                        tasks[row][1] = assignee_input
                        write_task('tasks.txt', 'a+')
                        return False
                    elif options == "4":
                        return False
                    else:
                        print("\nError: Invalid input. Please enter an option from the menu provided")
                        continue
            print('\nError: invalid input. Please try again.')
                
# Define view my tasks function to display only tasks assigned to user. Loop through each sub list of tasks
# and if assignee in tasks matches current user then print

def view_mine():
    rows = len(tasks)
    for row in range(rows):
        if tasks[row][1] == current_user[0]:
            print(
            "\nTask ID: \t\t" + str(tasks[row][0]) +
            "\nTask: \t\t\t" + str(tasks[row][2]) +
            "\nAssigned to: \t\t" + str(tasks[row][1]) +
            "\nDate assigned: \t\t" + str(tasks[row][4]) +
            "\nDue date: \t\t" + str(tasks[row][5]) +
            "\nTask complete? \t\t" + str(tasks[row][6]) +
            "\nTask description: \t" + str(tasks[row][3]) +
            "\n"
            )
        else:
            continue
    task_edit()

# Define task overview function to loop through tasks variable and count the number of tasks (outer list),
# increase complete counter if 'yes' in list or incomplete if not. If today's date is greater than due date,
# increase overdue counter 

def task_overview():
    wipe_file = open("task_overview.txt", "w")
    wipe_file.close()
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    today = datetime.strptime(today, "%d/%m/%Y")
        
    num_tasks = len(tasks)
    tasks_complete = 0
    tasks_incomplete = 0
    tasks_overdue = 0

    rows = len(tasks)
    for row in range(rows):
        if tasks[row][-1] == 'Yes':
            tasks_complete += 1
        else:
            tasks_incomplete += 1
            if datetime.strptime(tasks[row][-2], "%d/%m/%Y") < today:
                tasks_overdue += 1
            else:
                continue
        
    percent_incomplete = round((tasks_incomplete / num_tasks) * 100, 2)
    percent_overdue = round((tasks_overdue / num_tasks) * 100, 2)

    with open("task_overview.txt", "a+") as file:
        file.write(str(num_tasks) + ", " + str(tasks_complete) + ", " + str(tasks_incomplete) + ", " + str(tasks_overdue) + ", " + str(percent_incomplete) + ", " + str(percent_overdue) + "\n")
            

# Define user overview function to return number of users and tasks. Then loop through users and search for 
# them in tasks. Return the number of lines which they appear in as number of tasks. Calculate percentage of 
# tasks assigned to them. Determine whether task is complete, incomplete or overdue and calculate percentages. 
# Write to a new file 

def user_overview():
    new_file = open("user_overview.txt", "w")
    new_file.close()
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    today = datetime.strptime(today, "%d/%m/%Y")
    num_users = int(len(users) / 2)
    num_tasks = len(tasks)
    with open("user_overview.txt", "w") as f1:
        f1.write(str(num_users) + ", " + str(num_tasks) + "\n")
 
    given_user = []
    tasks_complete = 0
    tasks_incomplete = 0
    tasks_overdue = 0
    tasks_assigned = 0 

    counter = 0
    for user in users:
        if counter % 2 != 0:
            counter += 1
            continue
        else:
            rows = len(tasks)
            for row in range(rows):
                if user == tasks[row][1]:
                    given_user.append(user)
                    tasks_assigned += 1
                    if tasks[row][-1] == 'Yes':
                        tasks_complete += 1
                    else:
                        tasks_incomplete += 1
                        if datetime.strptime(tasks[row][-2], "%d/%m/%Y") < today:
                            tasks_overdue += 1
                        else:
                            continue
                else:
                    continue
        percent_tasks = round((tasks_assigned / num_tasks) * 100, 2)
        percent_complete = round((tasks_complete / tasks_assigned) * 100, 2) 
        percent_incomplete = round((tasks_incomplete / tasks_assigned) * 100, 2)
        percent_overdue = round((tasks_overdue / tasks_assigned) * 100, 2)
        with open("user_overview.txt", "a+") as f2:
            f2.write(str(given_user[0]) + ", " + str(tasks_assigned) + ", " + str(percent_tasks) + ", " + str(percent_complete) + ", " + str(percent_incomplete) + ", " + str(percent_overdue) + "\n")
            counter += 1
        given_user = []        
        tasks_complete = 0
        tasks_incomplete = 0
        tasks_overdue = 0
        tasks_assigned = 0 

# Define display statistics to print task_overview.txt and user_overview.txt in user-friendly manner if the 
# current user is admin

def display_statistics():
    task_stats = []
    if current_user[0] == "admin": 
        with open("task_overview.txt", "r") as f_tasks:
            lines = f_tasks.read().split(', ')
            print(
                "\nNumber of tasks: " + str(lines[0]) +
                "\nTasks complete: " + str(lines[1]) +
                "\nTasks incomplete: " + str(lines[2]) +
                "\nTasks overdue: " + str(lines[3]) +
                "\nPercentage incomplete: " + str(lines[4]) +
                "\nPercentage overdue: " + str(lines[5])
                )
        with open("user_overview.txt", "r") as f_users:
            lines = f_users.read().splitlines()
            for line in lines:
                temp2 = line.split(', ')
                task_stats.append(temp2)
            rows = len(task_stats)
            for row in range(rows):
                if len(task_stats[row]) < 3:
                    print(
                        "\nUsers registered: " + str(task_stats[row][0]) + "\n"
                        "Number of tasks: " + str(task_stats[row][1]) + "\n"
                        )
                else:
                    print(
                        "\nUser: " + str(task_stats[row][0]) + "\n" +
                        "Number of tasks: " + str(task_stats[row][1]) + "\n" +
                        "Percentage of tasks assigned to user: " + str(task_stats[row][2]) + "\n" +
                        "Percentage complete: " + str(task_stats[row][3]) + "\n" +
                        "Percentage incomplete: " + str(task_stats[row][4]) + "\n" +
                        "Percentage overdue: " + str(task_stats[row][5]) + "\n"
                    )
    else:
        print("\nYou are not authorised to perform this action")
            

# Define exit function to print goodbye message then exit programme

def exit_programme():
    print("\nGoodbye!")
    exit()

# Present the menu to the user and convert inputs to lower case.

login()    
                
while True:
    
    menu = input("""\nSelect one of the following Options below:\n
r - Register a user
a - Add a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
""").lower()

# Call menu functions:

    if menu == "r":
        register()
    elif menu == "a":
        add_task()
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()
    elif menu == "gr":
        task_overview()
        user_overview()
    elif menu == "ds":
        display_statistics()
    elif menu == "e":
        exit_programme()
        
# If user enters any other input, print error message

    else:
        print("\nError: invalid input. Please enter a command from the menu provided.")