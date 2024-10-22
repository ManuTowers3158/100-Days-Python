
#   - Use the `count` function to display the number of each item when viewing the inventory.
#


import os
import time


def check_duplicates(item):
    if item in inventory:
        #print("Item already in agenda")
        time.sleep(2)
        return True
    else:
        return False
def printList():
    print()
    aux_list=[]
    for item in inventory:
        if item not in aux_list:
            item_count=inventory.count(item)
            print(item,"x",item_count)
            aux_list.append(item)
    print()


inventory=[]
aux_list=[]
debug=True
try:
    f=open("Support Files/Inventory.txt","r")
    inventory=eval(f.read())
    f.close()
except Exception as err:
    print("Jefe su archivo no existe")
    if debug==True:
        print(err)
    time.sleep(3)
x=True
while x==True:
    os.system("cls")
    print("=========Inventory========")
    menu=input("1.Add Items\n2.View Items\n3.Remove Items\nX. Exit\n>>> ")
    if menu=="1":
        os.system("cls")
        item = input("What do you want to add?:\n>>>  ")
        item=item.capitalize()
        inventory.append(item)
        print("item added")

        f = open("Support Files/Inventory.txt", "w")
        f.write(str(inventory))
        f.close()

        time.sleep(3)


    elif menu == "2":
        os.system("cls")
        print("Your current inventory is: ")
        printList()
        time.sleep(3)

    elif menu == "3":
        os.system("cls")
        print("Current inventory is:")
        #print(inventory)
        printList()
        item = input("What do you want to delete?:\n>>>  ")
        item=item.capitalize()
        if item in inventory:
            confirmation = input("Are you sure you want to Delete it?:\n1.Yes\n2.No\n>>>")
            if confirmation == "1":
                inventory.remove(item)
                print("Item removed")

                f = open("Support Files/Inventory.txt", "w")
                f.write(str(inventory))
                f.close()

                time.sleep(2)
    else:
        x=False
        break