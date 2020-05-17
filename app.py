import getpass
users = {}
answer = ""

def initial_menu():
    answer = input("Are you already registered? y/n (press q to quit) ")
    if answer == "y":
        existing_user()
    elif answer == "n":
        new_user()
    elif answer == "q":
        print("bye bye")
    else:
        print("Please enter either y or n.")
        initial_menu()


def existing_user():
    check_user = input ("Please enter your username: ")
    check_password = getpass.getpass("Please enter your password: ")
    if check_user in users and check_password == users[check_user]:
        print("login succesful")
        initial_menu()
    else:
        print("username or password incorrect...returning to main menu")
        initial_menu()



def new_user():
    user_name = input("Please enter a username: ")
    if user_name in users:
        print("this username already exists.")
        new_user()
    else:
        password = getpass.getpass("Please enter a password: ")
        users[user_name] = password
        print("Thanks for registering...returning to main menu")
        initial_menu()

initial_menu()
