import time
import random
total_score = 0
animals = ["Bird", "Cat", "Squirrel"]

def print_pause(phrase):
    """
    This function print the phrase I passes it and pause 3 seconds
    """
    print(phrase)
    time.sleep(3)

def Game():
    """
    This function run the game
    """
    print_pause("You were sitting in your home when"
            " you heard screams from the outside.")
    print_pause("You wondered what's happening outside"
            " and you couldn't hold your curiosity...")
    print_pause("You decided to gather your courage"
            " and all the needed supplies including your knife.")
    print_pause("You went outside to see what's going on!")
    print_pause("You found the nearby area to your house is being restricted"
            " and surrounded by fences.")
    print_pause("Three kilometers away there is a forest")

    print_pause("Enter 1 to enter the restricted area.")
    print_pause("Enter 2 to walk to the forest.")
    print_pause("What would you like to do ?")
    user_input = input("(Please enter 1 or 2).")
    while user_input != "1" or user_input != "2":

        if user_input == "1":
            Restricted_area(total_score)
            break
        elif user_input == "2":
            Forest()
            break
        user_input = input("(Please enter 1 or 2)")

def Restricted_area(score):
    """
    This function do consequences if the 
    player enters the restrictied area 
    """
    print_pause("When you had approached the restricted area"
                " you encountered police officers.")
    print_pause("They prevented you from entering the area.") 
    print_pause("You returned back to your house.")
    score -= 4
    total_score = score
    print_pause("Your score has decremented by 4 points.")
    print("You have lost of score",total_score,"/10.")
    print_pause("Would you like to play again?")
    choice = input("(y/n): ")
    while choice != "y" or choice != "n":

        if choice == "y":
            Game()
        elif choice == "n":
            break
        choice = input("Please enter (y/n): ")

def directions(score):
    """
    This function prompts the player to choose a direction to enter
    and based on the player's choice there's consequences
    """
    print_pause("Enter 1 to go left.")
    print_pause("Enter 2 to go right.")
    user_input = input("(Please enter 1 or 2)")
    while user_input != "1" or user_input != "2":
         
        if user_input == "1":
            print_pause("You went left.")
            score -= 1
            total_score = score
            print_pause("Your score has decremented by 1 point.")
            print("Your score is",total_score,"/10.")
            print_pause("GAME OVER!!")
            print("You have lost of score",total_score,"/10.")
            break
        elif user_input == "2":
            print_pause("You went right.")
            score += 1
            total_score = score
            print_pause("Your score incremented by 1 point.")
            print("Your score is",total_score,"/10.")
            print_pause("You entered a shortcut exit.")
            print_pause("You found a communication device with aliens")
            print_pause("You walked a few more kilometers.")
            print_pause("You found an alien spaceship infront of you.")
            score += 2
            total_score = score
            print_pause("Your score has incremented by 2 points.")
            print("Your score is",total_score,"/10.")
            print_pause("You met an alien in your way"
                        " and communicated with him with the device.")
            print_pause("Thereafter the aliens became friends"
                        " with the humankind.")
            score += 3
            total_score = score

            print_pause("Your score has incremented by 3 points.")
            print("Your score is",total_score,"/10.")
            print_pause("GAME Over!!")
            print("You have won of score",total_score,"/10.")
            break
        user_input = input("(Please enter 1 or 2) ")

    print_pause("Would you like to play again?")
    choice = input("(y/n): ")
    while choice != "y" or choice != "n":

        if choice == "y":
            Game()
        elif choice == "n":
            break
        choice = input("Please enter (y/n): ")

def injured_animal(score):
    """
    This function asks the player to choose
    if he wants to help the injured player 
    """
    print_pause("Enter 1 to help the injured animal.")
    print_pause("Enter 2 to leave the animal.")
    user_input = input("(Please enter 1 or 2)")
    while user_input != 1 or user_input != 2:

        if user_input == "1":
            print_pause("You helped the injured animal.")
            print_pause("You knew from the animal"
                         " that there is something have penetrated our planet.")
            score += 2
            total_score = score
            print_pause("Your score has incremented by 2 points.")
            print("Your score is",total_score,"/10.")
            break
        elif user_input == "2":
            print_pause("You left the animal.")
            score -= 2
            total_score = score
            print_pause("Your score has decremented by 2 points.")
            print("Your score is",total_score,"/10.")
            break
        user_input = input("(Please enter 1 or 2) ")

    print_pause("You lost your way home"
                " and you have prepared your weapon in reserve.")
    directions(total_score)
 
def a_sound(score):
    """
    This function asks the player 
    if he wants to investigate the sound he is hearing
    """
    print_pause("Enter 1 to go investigate the sound.")
    print_pause("Enter 2 to ignore the sound and keep moving.")
    user_input = input("(Please enter 1 or 2)")
    while user_input != "1" or user_input != "2":

        if user_input == "1":
            print_pause("You went to investigate the sound.")
            score += 1
            total_score = score
            print_pause("Your score has incremented by 1 point.")
            print("Your score is",total_score,"/10.")
            animal = random.choice(animals)
            print("You found an injured", animal)
            score += 1
            total_score = score
            print_pause("Your score has incremented by 1 point.")
            print("Your score is",total_score,"/10.")
            injured_animal(total_score)
            break
        elif user_input == "2":
            print_pause("You ignored the sound and kept moving.")
            score -= 1
            total_score = score
            print_pause("Your score has decremented by 1")
            print("Your score is",total_score,"/10.")
            print_pause("You lost your way home.")
            directions(total_score)
            break
        user_input = input("(Please enter 1 or 2): ")
            
            
def Forest():
    """
    This function do consequences if the 
    player enters the Forest
    """
    print_pause("You walked to the forest.")
    print_pause("You hear a sound from far away.")
    a_sound(total_score)
    

Game()

