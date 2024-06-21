import turtle
import time
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import *

from tkinter import ttk

WIDTH,HEIGHT = 500,500
COLORS = ['red','green','blue','orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def init():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtles Racing")

Turtles = []

def get_racers():
    racers = input('Enter the number of races [2-10] included\n')
    while True:
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input contains invalid characters. Please only enter integers',end="\n")
        if 2 <= racers <= 10:
            return racers
        else:
            print('Invalid amount of racers entered. Please try again',end="\n")
        racers = input('Enter the number of races [2-10] included\n')
    return racers

def create_turtles(color):
    length = len(color)+1
    turtles = []
    for i, color in enumerate(color):
        x = (WIDTH // length *(i+1)) -WIDTH//2
        print(x)
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #set pos
        racer.setpos(x,-HEIGHT//2+25)
        racer.pendown()
        turtles.append(racer)
    return turtles

#racers = get_racers()
#racer = turtle.Turtle()
#racer.penup()
#racer.color('cyan')
#racer.shape('turtle')
#racer.forward(100)



racer_count = get_racers()


random.shuffle(COLORS)
colors = COLORS[:racer_count]

str = "Choose your bet"
str2="Choose one of the following colors to bet on "
messagebox.showinfo(title=str,message=str2)

win = tk.Tk()
win.geometry("400x400")

colors_string = "colors:\n"+ "\n".join(colors)

global colorChosen
colorChosen = ""

# Define a function to return the Input data
def get_data():
    colorChosen = entry.get() #problem, colorhosen changes here but not in the outer loop
    if(colorChosen in colors):
        win.withdraw()

        str = "Bet results: " + colorChosen
        str2 = "You have chosen to bet on: " + colorChosen
        messagebox.showinfo(title=str, message=str2)

        init()

        racers = create_turtles(colors)
        bool = False;
        color = None

        while bool is False:
            for racer in racers:
                x, y = racer.pos()
                step = random.randint(1, HEIGHT // 14)
                if (step + y > HEIGHT / 2): step = HEIGHT / 2 - y - 20
                racer.pendown()
                racer.forward(step)
                if (y > HEIGHT / 2 - 20):
                    bool = True
                    i, color = racer.color()
                    break

            time.sleep(0.05)
        if(color == colorChosen):
            str = "WON"
            str2 = "Your TURTLE IS THE WINNEER: " + color
        else:
            str = "LOST"
            str2 = "Your TURTLE has failed.\nTHEE WINNNEER IIIS: " + color
        messagebox.showinfo(title=str, message=str2)

        print("Game has ended")

        win.destroy()
    else:
        label.config(text="Wrong color entered. Please try again\n"+colors_string, font= ('Helvetica 13'))

#Create an Entry Widget
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(win, text=colors_string, font=('Helvetica 13'))
label.pack()

#Create a Button to get the input data
ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)

win.mainloop() #ensures the init starts after this part

turtle.mainloop() # prevent the screen from closing