import getpass

username = "Barry"
password = "dru"

def login_athenticator():
    entered_username = input("Please enter your username:")
    entered_password = getpass.getpass()
    if entered_username == username and entered_password == password:
        print("access granted")
    else:
        print("access denied")
        return login_athenticator()



login_athenticator()