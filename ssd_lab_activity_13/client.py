import requests
import json

def signin():
    email = input("Enter email")
    password= input("Enter password: ")

    payload = {
        "email": email, 
        "password": password
    }
    resp = requests.post("http://127.0.0.1:8000/user/signin", json = payload).content.decode()

    print(resp)

def signup():
    username = input("Enter username: ") 
    password = input("Enter password: ")
    email = input("Enter email: ")

    payload = {
        "username": username, 
        "password": password,
        "email": email
    }
    resp = requests.post("http://127.0.0.1:8000/user/signup", json = payload).content.decode()
    print(resp)

def signout():
    resp = requests.get("http://127.0.0.1:8000/user/signout")
    print(resp)

while True:
    option = input("Enter option: \n1. Signup\n2. SignIn\n3. SignOut\n")
    if(option == "1"):
        signup()
    elif(option == "2"):
        signin()
    elif(option == "3"):
        signout()