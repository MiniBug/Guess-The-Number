# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
num_range = 100

# helper function to start and restart the game
def new_game():
    global secret_num, tries_left
    tries_left = 7
    secret_num = random.randrange(0, num_range)
    print "\nNew game. Range is from 0 to", num_range
    if num_range == 1000:
        tries_left = 10
    print "Number of remaining guesses is", tries_left
    
# define event handlers for control panel
def range100():
    global num_range
    new_game()
 
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    tries_left = 10
    new_game()
   
def get_input(guess):
    input_field.set_text("")
    guessed = False
    global tries_left
    global secret_num
    tries_left -= 1
    if tries_left == 0 and guessed == False:
            print "\nGuess was", guess,"\nNumber of remaining guesses is", tries_left,"\n","You ran out of guesses. The number was",secret_num
            new_game()
            return None
    elif tries_left >= 0:
        guess = int(guess)
        print "\nGuess was", guess
        print "Number of remaining guesses is", tries_left
        if guess == secret_num:
            print "Corect!"
            guessed = True
        if guess < secret_num:
            print "Higher!"
        if guess > secret_num:
            print "Lower!"
        if guessed:
                new_game()
        
    
# create frame
frame = simplegui.create_frame('Riddle Challenge! R U up 2?', 300, 300)
# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
input_field = frame.add_input('Enter a guess', get_input, 200)

# call new_game and start frame
new_game()
frame.start()
# always remember to check your completed program against the grading rubric
