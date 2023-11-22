print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______s/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice = input(
    "You see one path to the left and another to the right, where do you go?\n"
)
if choice == "left" or choice == "l" or choice == "LEFT" or choice == "L":
    print("You are alive... for now.")
    choice = input(
        "You see a big lake, but the water is getting lower. Do you wait or swim?\n"
    )
    if choice == "wait" or choice == "WAIT" or choice == "w" or choice == "W":
        print("Now you can get accross the lake.")
        choice = input(
            "You see red, blue and yellow doors, where do you go?\n")
        if choice == "red" or choice == "RED" or choice == "r" or choice == "R":
            print("You are burned by fire. Game over")
        elif choice == "blue" or choice == "BLUE" or choice == "b" or choice == "B":
            print("You are eaten by beasts. Game over.")
        elif choice == "yellow" or choice == "YELLOW" or choice == "y" or choice == "Y":
            print("Congratulations! You win!")
        else:
            print("Game over.")
    else:
        print("You are attacked by trout. Game over.")

else:
    print("You fall into a hole. Game over.")
