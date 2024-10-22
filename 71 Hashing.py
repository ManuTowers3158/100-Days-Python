import hashlib
import time
from tinydb import TinyDB, Query
import datetime
import os
import random

db = TinyDB('./Support Files/Users_data_base.json')
User = Query()
#*******Basic password settings**********
# password = "Mamnu"
# salt = "3158"
# newPassword = f"{password}{salt}"
# newPassword =  hashlib.sha256(newPassword.encode()).hexdigest()
#
# print(newPassword)
# # Insert a record
# db.insert({'name': 'Manu', 'password': newPassword, 'salt': salt})
#
#******Menu********
while True:
    print("Login portal")
    menu = input("1. Add Username \n2. User Login\n>>> ")
    if menu == "1":
        user = input("Provide username: ")
        password = input("New Password: ")
        salt = random.randint(0,1000)
        print(f"User: {user},Password {password},Salt: {salt}")
        newPassword = f"{password}{salt}"
        newPassword = hashlib.sha256(newPassword.encode()).hexdigest()
        print(newPassword)
        # Insert a record
        db.insert({'name': user, 'password': newPassword, 'salt': salt})

    if menu == "2":
        user = input("Enter username: ")
        result = db.search(User.name == user)
        ans = input("Enter Password: ")
        salt = result[0]['salt']
        password_original = result[0]["password"]
        print(salt)
        newPassword = f"{ans}{salt}"
        print(newPassword)
        newPassword = hashlib.sha256(newPassword.encode()).hexdigest()
        print(newPassword)
        if newPassword == password_original:
            print("Welcome aboard Captain Torres, all systems ready to engage")






