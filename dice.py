# Welcome to Dice!
# written by bryan hamilton 01/23/25
# coded using Python 3.13.1 under the Windows 10 enviorment. 
# 
# This is a simple dice game.  
# 
# The object of the game is to roll the dice and guess the rolled number (1-100).
# You have a correct guess in under 5 attempts or the game will end.
# Upon game restart,  It will randomizes a new number to guess thus starting fresh. 
#
# good luck, have fun!

# import random and os






import random
import os 
import sys
import time
from termcolor import colored, cprint

# define center of screen.
def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    print(text.center(terminal_width))

# define exit function (quit the application good 'n propper)
def exit_program():
    os.system('clear')
    
    space_count = 0
    while True: 
        print_centered(msg_space)
        space_count += 1
        if space_count == 10:
            break
    
    print("\033[1;37m Exiting the Dice! program ...")
    space_count = 0
    while True: 
        print_centered(msg_space)
        space_count += 1
        if space_count == 10:
            break
    
    sys.exit(0)



# Welcoming messages
text_msg1 = ("\033[1;34m Welcome to my Dice!")
text_msg2 = ("\033[1;34m coding by:")
text_msg3 = ("\033[0;37m bryan hamilton")
text_msg4 = ("\033[0;40m 01/23/25")
text_msg5 = ("\033[1;36m I'm thinking of a number between 1 and 100.")

# congrats messags
win_msg1 = "Congratulations! You guessed the number in"

# using this as a sad attempt for screen locator.   will fix when i feel like it. 8-P
msg_space = " "

# sending the user YOU LOSE! game message. 
text_gameend_msg = ("\033[0;31m You maxed your guesses.  Game Over! ")



# build the game board
def play_game():
    os.system('clear')
    # define random number
    number = random.randint(1, 100)
    attempts = 0
    
    # set up center drop-text-down spaces
    space_count = 0
    while True: 
        print_centered(msg_space)
        space_count += 1
        if space_count == 10:
            break
    # display game and introduction messages.   
    print_centered(text_msg1)
    print_centered(text_msg2)
    print_centered(text_msg3)
    print_centered(text_msg4)
    
    # set up bottom-up spaces
    space_count = 0
    while True: 
        print_centered(msg_space)
        space_count += 1
        if space_count == 5:
            break
    print(text_msg5)
    






#--------------------------------------------------------------------------------------------------------------#        
    
    # Game loop & logic code. 
    while True:
        try:
            guess = int(input("Enter your guess: "))
        
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        # guess too low, clear screen, try again. 
        if guess < number:
            #os.system('clear')
            print_centered(msg_space)
            print_centered("Too low, try again!")
            
            time.sleep(1)
                                    
        # guess too high, clear screen, try again. 
        elif guess > number:
            
            print_centered(msg_space)
            print_centered("Too high, try again!")
            
            time.sleep(1)
         



        
        # guess spot on, clear screen and restart game.                         
        else:
            print(win_msg1,attempts, "attempts")
            
            time.sleep(2) # 2 second timing pause. 
            #os.system('clear')
            user_input = input("\033[0;31m Do you want to (C)ontinue or (Q)uit? (Q/C): ")
            if user_input.lower() == "q":
                    
                    exit_program()
            else:
            #clear question, continue with game.  Smash anykey to (C)ontinue.
                os.system('clear')
                play_game( )   
 




 # adding game-stop/gameover condition. 5 attemps & failed.
        if (attempts > 4): #5th attempt fail, ask user to quit or continue
            os.system('clear')
            print_centered(text_gameend_msg)
            time.sleep(3) # 3 second timing pause. 
            
        # added proper exit routine.       
        
            user_input = input("Do you want to (C)ontinue or (Q)uit? (Q/C): ")
            if user_input.lower() == "q":
                    
                    exit_program()
            else:
                          
                play_game( )   


# up we go, back to the top home boy.   ;) 
if __name__ == "__main__":
    play_game( )
