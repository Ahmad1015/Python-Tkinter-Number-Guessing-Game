# Import necessary libraries
import random
from tkinter import *

# Initialize global variables
randomNumber = -1
score = 10
flag3 = flag2 = flag5 = CheckFlag = False

# Create the main tkinter window
root = Tk()
root.geometry("700x200")

# Create and configure labels
ScoreBoard = Label(root, text="Score is:" + str(score), font="Arial 12 bold", foreground='blue')
Label(root, text="Guessing Game", font="Arial 12 bold", foreground='blue').grid(row=0, column=0)
message = Label(root, text="TRY YOUR LEVEL BEST", font="Arial 9 bold", foreground='Red')
OutputScreen = Label(root, text="Enter your Guess here", font="ar 10 bold")
OutputScreen.grid(row=2, column=0)

# Create a variable to store the user's input
Screen = StringVar()

# Create an input field
ScreenEntry = Entry(root, textvariable=Screen, width=39, font='ar 12 bold')
ScreenEntry.grid(row=2, column=1, pady=15)
ScoreBoard.grid(row=10, column=0)
message.grid(row=0, column=1)

# Initialize global variables function
def InitialiseGlobal():
    global randomNumber, flag2, flag3, flag5
    randomNumber = -1
    flag3 = flag2 = flag5 = False

# Generate a random number function
def rand():
    global randomNumber
    randomNumber = random.randint(0, 100)
    print(randomNumber)

# Provide clues based on the random number
def clue():
    global flag2, flag3, flag5
    if randomNumber % 2 == 0:
        flag2 = True
    if randomNumber % 3 == 0:
        flag3 = True
    if randomNumber % 5 == 0:
        flag5 = True

# Start the game
def start():
    InitialiseGlobal()
    rand()

# Handle providing clues to the user
def HandlingClue():
    global message, flag2, flag3, flag5, randomNumber,CheckFlag
    try:
        if randomNumber == -1:
            raise IndexError
        clue()
        choice = 'This one is a tricky one - Not a multiple of 2,3 or 5'
        if flag2 == True and flag3 == True and flag5 == True:
            choice = random.choice(['It is a multiple of 2', 'It is a multiple of 3', 'It is a multiple of 5'])
        elif flag2 == True and flag3 == True and flag5 == False:
            choice = random.choice(['It is a multiple of 2', 'It is a multiple of 3'])
        elif flag2 == True and flag3 == False and flag5 == False:
            choice = 'It is a multiple of 2'
        elif flag2 == False and flag3 == True and flag5 == True:
            choice = random.choice(['It is a multiple of 5', 'It is a multiple of 3'])
        elif flag2 == False and flag3 == True and flag5 == False:
            choice = 'It is a multiple of 3'
        elif flag2 == False and flag3 == False and flag5 == True:
            choice = 'It is a multiple of 5'
        message.grid_forget()
        message = Label(root, text=choice, foreground='Green', font='20')
        message.grid(row=0, column=1)
        CheckFlag = True
        health()
        CheckFlag=False
    except IndexError:
        message.grid_forget()
        message = Label(root, text="Cannot get help before trying first", foreground='Green', font='20')
        message.grid(row=0, column=1)

# Check if the user's guess is correct
def Check():
    global message, randomNumber
    temp = int(ScreenEntry.get())
    health()
    if randomNumber == temp:
        message.grid_forget()
        message = Label(root, text="Amazing you Guessed it correct", foreground='Green', font='20')
        message.grid(row=0, column=1)
    else:
        message.grid_forget()
        message = Label(root, text="Wrong Try again", foreground='Red', font='20')
        message.grid(row=0, column=1)

# Update the user's score
def health():
    global score, ScoreBoard, CheckFlag,message
    if CheckFlag:
        score -= 3
    else:
        score -= 1
    if score==0:
        message.grid_forget()
        message = Label(root, text="Game ended - Score is Zero", foreground='Red', font='20')
        message.grid(row=0, column=1)
    ScoreBoard.grid_forget()
    ScoreBoard = Label(root, text="Score is:" + str(score), font="Arial 12 bold", foreground='blue')
    ScoreBoard.grid(row=10, column=0)

# Create buttons for checking, starting, and getting help
Button(text="Check", command=Check, background='gray', foreground='blue', font='ar 20 bold').grid(row=7, column=1)
Button(text="Start", command=start, background='gray', foreground='blue', font='ar 20 bold').grid(row=7, column=0)
Button(text="Need Help", command=HandlingClue, background='gray', foreground='blue', font='ar 20 bold').grid(row=7,
                                                                                                             column=2)

# Run the main loop
root.mainloop()
