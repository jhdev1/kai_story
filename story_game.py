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
    print("Where its heart should have been was a sighn that said: Take the right one and you shall move on and find the treasure you want, use your brain and you shall servive.")
    print("")

    first = input("What do you do? Do you take snake or take potion ")
    print("")
    if first.lower() == ("take potion"):
        print("The statue moves and squishes you.")
        print("")
        die = input("Do you want to continue y/n")
        
        if die.lower()==("n"):
            quit(1)
        if die.lower()==("y"):
            loop=1
            clear_screen()
            print("Your soul possesed another adventurer and you go in front of the cave.")
            print("")
            
    if first.lower() == ("take snake"):
        print("")
        print("You chose wisely and you move on into a cave that opened in front of you.")
        print("")
        loop=2
    else:
        loop==1
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
    
    if second.lower() == ("take gun"):
        print("")
        print("As you take it, the other things sink into the wall and the floor moves forward.")
        print("")
        print("Out of the dark, something lunges at you and kills you.")
        print("")
    elif second.lower()==("take knife"):
        print("")
        print("As you take it, the other things sink into the wall and the floor moves forward.")
        print("")
        print("Out of the dark, something lunges at you and kills you.")
        print("")    
        dies = input("Do you want to continue y/n")
        
        if dies.lower()==("n"):
            quit(1)
        if dies.lower()==("y"):
            loop = 2
            clear_screen()
            print("")
            print("Your soul possesed another wise adventurer and you enter the cave")
            print("")
            
    elif second.lower()== ("take torch"):
        print("As you take it the other things sink into the wall and the floor moves forward.")
        print("")
        print("Using the light of a torch, you see a hairy beast come at you and you quickly use the torch to burn it to ashes.")
        print("")
        print("When the floor stops moving you see two paths.")
        print("")
        

        
        
        while loop == 2:
            path = input("Which way will you go,right or left")
            if path.lower()==("right"):
                print("")
                print("As you enter the right path, a wall closes the way back.")
                print("")
                print("You had no choice but to move on.")
                loop=3
            elif path.lower()==("left"):
                print("")
                print("As you enter the left path, a wall closes the way back.")
                print("")
                print("You had no choice but to move on.")
                loop=4
            else:
                print("")
                print("")
                print("Please enter one of the choices. Enter it exactly.")
                print("")
            
            
    elif second.lower()==("move on"):
        print("")
        print("You move on and realized there was a huge hole in front of you.")
        print("")
        print("You had a slow reacion and you fell into the hole")
        loop=5
    else:
        print("")
        print("")
        print("Please enter one of the choices. Enter it exactly.")
        loop=2
        
while loop==3:
    print("")
    print("As you go deeper into the tunnel, you make out thousands of skelotons embedded in the walls.")
    print("")
    print("At the end, you see a large ancient door that leads to the treasure.")
    print("")
    print("Before you can move on you had to solve three questions.")
    print("")
    print("You had to solve the questions in order to solve the puzzle.")
    print("")
    print("The three questions were:")
    print("")
    print("I have four legs, a shell, and I am very slow. What am I?")
    print("")
    print("Suddenly three animals pop out of the ground.")
    print("")
    print("They are a turtle, a snail, and a elaphant.")
    print("")
    three=input("Which do you choose?")
    if three.lower==("turtle"):
        print("The door slides open, but there is a door behind it.")
    if three.lower==("snail"):
        print("The snail morphed into a lion and killed you.")
        dies = input("Do you want to continue y/n")
        if dies.lower()==("n"):
            quit(1)
        if dies.lower()==("y"):
            loop = 2
            clear_screen()
         
    if three.lower==("snail"):
        print("The elaphant morphed into a cheeta and killed you.")
        dies = input("Do you want to continue y/n")
        if dies.lower()==("n"):
            quit(1)
        if dies.lower()==("y"):
            loop = 2
            clear_screen()
            

    
    
    
     
    
