import getpass
users = {}

def initial_menu():
    answer = input("Are you already registered? Y/N: ")
    if answer == "y":
        existing_user()
    elif answer == "n":
        new_user()
    else:
        print("Please enter either Y or N.")
        initial_menu()


def existing_user():
    check_user = input ("Please enter your username: ")
    if check_user in users:
        check_password = input ("Please enter your password: ")
        check_password = users[check_user]
        print("login succesful")
    elif check_user not in users:
        print("username already in use...returning to main menu")
        initial_menu()



def new_user():
    user_name = input("Please enter a username: ")
    if user_name in users:
        print("this username already exists.")
        new_user()
    else:
        password = input("Please enter a password: ")
        users[user_name] = password
        existing_user()

initial_menu()


