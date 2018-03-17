import string
import os
loop = 1
def clear_screen():
    print("\n"*2)
    
while loop ==1:
    print("You are standing in front of a huge statue that is holding one thing in each hand.")
    print("")
    print("In one hand it was holding a potion of immortality and in the other hand, it was holding a snake.")
    print("")
    print("Where its heart should have been was a sighn that said: Take the right one and you shall move on and find the treasure you want, use your brain and you shall survive.")
    print("")
    first = input("What do you do? Do you take snake or take potion ")
    print("")
    if first.lower() == "take potion":
        print("The statue moves and squishes you.")
        print("")
        die = input("Do you want to continue y/n")
        
        if die.lower()=="n":
            quit(1)
        if die.lower()=="y":
            loop=1
            clear_screen()
            print("Your soul possesed another adventurer and you go in front of the cave.")
            print("")
            
    elif first.lower() == "take snake":
        print("You chose wisely and you move on into a cave that opened in front of you.")
        print("")
        print("")
        print("")
        loop=2
    else:
        loop=1
        print("")
        print("")
        print("Please enter one of the choices. Enter it exactly")
        print("")


while loop ==2:
    print("When you enter the cave, you see darkness all around you.")
    print("")
    print("The only light comes from a torch.")
    print("")
    print("You see movement deeper in the cave, but you can't make out what it is.")
    print("")
    print("Next to the torch is a knife and a gun.")
    print("")
    second=input("What do you do? Do you take gun, take knife, move on, or take torch")
    
    if second.lower() == "take gun":
        print("")
        print("As you take it, the other things sink into the wall and the floor moves forward.")
        print("")
        print("Out of the dark, something lunges at you and kills you.")
        print("")
    elif second.lower()=="take knife":
        print("")
        print("As you take it, the other things sink into the wall and the floor moves forward.")
        print("")
        print("Out of the dark, something lunges at you and kills you.")
        print("")    
        dies = input("Do you want to continue y/n")
        
        if dies.lower()=="n":
            quit(1)
        if dies.lower()=="y":
            loop = 2
            clear_screen()
            print("")
            print("Your soul possesed another wise adventurer and you enter the cave")
            print("")
            
    elif second.lower()== "take torch":
        print("As you take it the other things sink into the wall and the floor moves forward.")
        print("")
        print("Using the light of a torch, you see a hairy beast come at you and you quickly use the torch to burn it to ashes.")
        print("")
        print("When the floor stops moving you see two paths.")
        print("")
        

        
        
        while loop == 2:
            path = input("Which way will you go,right or left")
            if path.lower()=="right":
                print("")
                print("As you enter the right path, a wall closes the way back.")
                print("")
                print("You had no choice but to move on.")
                loop=3
            elif path.lower()=="left":
                print("")
                print("As you enter the left path, a wall closes the way back.")
                print("")
                print("You had no choice but to move on.")
                loop=3
            else:
                print("")
                print("")
                print("Please enter one of the choices. Enter it exactly.")
                print("")
            
            
    elif second.lower()=="move on":
        print("")
        print("You move on and realized there was a huge hole in front of you.")
        print("")
        print("You had a slow reacion and you fell into the hole")
        loop=3
    else:
        print("")
        print("")
        print("Please enter one of the choices. Enter it exactly.")
        loop=2
        
while loop==3:
    print("")
    print("As you go deeper, you make out thousands of skelotons embedded in the walls.")
    print("")
    print("At the end, you see a large ancient door that leads to the treasure.")
    print("")
    print("Before you can move on you had to solve three questions.")
    print("")
    print("You had to solve the questions in order to solve the puzzle.")
    print("")
    print("The first riddle is: I have four legs, a shell, and I am very slow. What am I?")
    print("")
    print("Suddenly three animals pop out of the ground.")
    print("")
    print("They are a turtle, a snail, and a elaphant.")
    print("")
    three=input("Which do you choose? Turtle, snail, or elaphant?")
    if three.lower()=="turtle":
        print("")
        print("The door slides open, but there is a door behind it.")
        print("")
        loop=4
        
    if three.lower()=="snail":
        print("The snail morphed into a wolf and killed you.")
        dies = input("Do you want to continue y/n")
        if dies.lower()=="n":
            quit(1)
        if dies.lower()=="y":
            loop = 3
            clear_screen()
         
    if three.lower=="elephant":
        print("The elaphant morphed into a fox and killed you.")
        diess = input("Do you want to continue y/n")
        if diess.lower()=="n":
            quit(1)
        if diess.lower()=="y":
            loop = 3
            clear_screen()
    else:
        print("")
        print("")
        print("Please enter one of the choices. Enter it exactly.")
        loop=3

while loop==4:
    print("The second riddle is: I have a mane and I have the most powerful roar. What am I?")
    print("")
    print("Suddenly another four animals popped up.")
    print("")
    print("They were a horse, a lion, a rino, and a snake.")
    print("")
        
    four=input("Which do you choose? horse, lion, rino, or snake?")
    if four.lower()=="horse":
        print("The horse morphed into a scorpion and killed you.")
        print("")
        diess = input("Do you want to continue y/n")
        if diess.lower()=="n":
            quit(1)
        if diess.lower()=="y":
            loop = 4
            clear_screen()
            
    if four.lower()=="lion":
        print("The second door slid open, but there was one more behind it.")
        print("")
        loop=5

    if four.lower()=="rino":
        print("The rino got angry, rammed into you, and killed you.")
        diesss = input("Do you want to continue y/n")
        if diesss.lower()=="n":
            quit(1)
        if diesss.lower()=="y":
            loop = 4
            clear_screen()
            
    if four. lower()=="snake":
        print("The snake grew larger, ate you, and killed you.")
        diessss = input("Do you want to continue y/n")
        if diessss.lower()=="n":
            quit(1)
        if diessss.lower()=="y":
            loop = 4
            clear_screen()    

    else:
        print("")
        print("")
        print("Please enter one of the choices. Enter it exactly.")
        loop=4
            

while loop==5:
    print("The third riddle is: I am a food, I am ood with syrup, and I can be made with a pan and a cake put together. What am I?")
    print("")
    print("You must at one food, beware if you eat the wrong one, it will be poisened.")
    print("")
    print("Suddenly five foods popped up. It was a cake, a muffin, a pancake, a steak, and pork.")
    print("")
    five = input("Which do you eat? Cake,  muffin,  pancake,  steak, or pork.")
    if five.lower()=="pancake":
        print("The last door opened and you walk into a bright shiny room filled with crystals.")
        print("")
        print("In the middle of the room was one piece of a very old artifact. It seemed to be missing two pieces.")
        print("")
        print("When you take it, you were wiped unconsious by an invisible force.")
        print("")
        print("When you wake up, you were standing in front of the statue.")
        print("")
        print("Now you shall continue your journy to find the other two pieces.")
        print("")

    else:
        ("This food is poisened and you died.")
        die = input("Do you want to continue y/n")
        if die.lower()=="n":
            quit(1)
        if die.lower()=="y":
            loop = 5
            clear_screen()
            print("Your soul possesed another wize adventurer.")        
    
        
    
            

    
    
    
     
    
