import requests
import getpass
from gui import display

BASE_URL = "http://172.16.159.132:8080/"

def display_menu():
    print("----- User Menu -----")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def register():
    print("----- Register -----")

    first_name = input("Enter first name: ")
    last_name  = input("Enter last name: ")
    username   = input("Enter username: ")
    password = getpass.getpass("Enter password: ")


    data = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'password': password
    }

    response = requests.post(f"{BASE_URL}/register", data=data)

    if (response.status_code == 200):
        print("Successfully registered!")
    else:
        print("Registration failed!")


def login():
    print("----- Login -----")

    username   = input("Enter username: ")
    password = getpass.getpass("Enter password: ")


    data = {
        'username': username,
        'password': password
    }

    response = requests.post(f"{BASE_URL}/login", data=data)

    if (response.status_code == 200):
        print("Successfully logged in!")
        display(username)
    else:
        print("Login failed!")


def main():

    runMain = True

    while(runMain):

        choice = display_menu()

        if (choice == '1'):
            register()
        elif (choice == '2'):
            login()
        elif (choice == '3'):
            runMain = False
            print("Good Day!")
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
