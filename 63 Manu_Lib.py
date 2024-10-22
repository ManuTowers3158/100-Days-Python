def contrasena(password):
    array1 = []
    array2 = []
    password_def = ["Manuguapo3158"]
    for i in password:
        array1.append(i)
    print(array1)


    for i in password_def[0]:
        array2.append(i)
    print(array2)
    flag=True
    for i in range(len(array2)):
        try:
            if array1[i] != array2[i]:
                flag = False
        except:
                flag = False
    if flag == True:
        return True
    else:
        return False

def palindrome(word):
    if len(word)<=1:
        return True
    if word[0] != word [-1]:
        return False
    return palindrome(word[1:-1])

def reverse(value):
    if value <=0:
        print("Done!")
        return
    else:
        for i in range(value):
            print("#",end="")
        print()
        reverse(value-1)
def factorial(value):
    if value <=0:
        print("Done!")
        return
    else:
        factorial_value=0
        for i in range(value+1):
            current_value=i
            factorial_value=factorial_value+current_value
        factorial(value-1)
    return factorial_value

def prettyPrint(list2D):
    print()
    for row in list2D:
        for item in row:
            print(f"{item:^10}",end=" | ")
            break
        print()
    print()

def changeColor(color, word):
    if color =="red":
        print("\033[31m", word, sep="", end="")
    elif color=="green":
        print("\033[32m", word, sep="", end="")
    elif color=="blue":
        print("\033[34m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="", end="")

def AreaTriangle (base, height):
    area=(base*height)/2
    return area

def play_sound(sound_file):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def sixRoll():
    import random
    sixvalue = random.randint(1, 6)
    return sixvalue