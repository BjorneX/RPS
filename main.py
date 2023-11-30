import random
import math
import tkinter as tk
import sys
from tkinter import font
import keyboard

def redirect_output(text_widget):
    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, message):
            self.text_widget.insert(tk.END, message)
            self.text_widget.see(tk.END)  # Scroll to the end of the Text widget

    sys.stdout = StdoutRedirector(text_widget)

# Create the main window
window = tk.Tk()
window.title("Output")

# Set window background color to #222222
bgcolor = "#222222"
window.configure(bg=bgcolor)

# Create a Text widget to display the output
output_text = tk.Text(window, height=20, width=50, bg=bgcolor, fg='white')
output_text.pack()

# Redirect Python output to the Text widget
redirect_output(output_text)

# Calculate the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the window's width and height
window_width = 500
window_height = 400

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set the window's geometry
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Center the Text widget
output_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Eventually add area of boxes option and starting number

#Variables

Score = 0

Field = [0,0,0,0,
         0,0,0,0,
         0,0,0,0,
         0,0,0,0,]

game_activation = False

col = [False, False, False, False]
row = [False, False, False, False]

#Visuals (I legobitar)

print("Press 'space' to start the game of 2048!\n")

#while(Score!=2048):

def Generate(): # Generera random 2a
    global RandomSquare

    RandomSquare = random.randint(0, len(Field)-1) 

    if Field[RandomSquare] == 2:
        RandomSquare = random.randint(0, len(Field)-1)

    Field[RandomSquare] = 2

def output():

    # Fixa 2 vid start

    output_text.delete(1.0, tk.END)

    field_size = int(math.sqrt(len(Field)))

    for i in range(0, len(Field), field_size):
        for j in range(field_size):
            print(Field[i+j], end=' ')
        print()

def w_key(event):

    global Determined_Square, RandomSquare #Hämta från global

    output_text.delete(1.0, tk.END)

    # Fixa kollision och andra 2ans rörelse


    Determined_Square = int(RandomSquare % math.sqrt(len(Field)))

    Field[RandomSquare] = 0 # Ta bort 2a

    if Field[Determined_Square] == 2:
        Field[Determined_Square] *= 2  # Multiply by 2
        Generate()  # Generate a new 2 after multiplication
        
    else:
        Field[RandomSquare] = 0
        Field[Determined_Square] = 2
        Generate()  # Generate a new RandomSquare

    output() # Output the updated field



def space_key(event):
   global game_activation
   if not game_activation: # Fråga samuel, blir det inte true?
       game_activation = True
       output()

def find_position(matrix, target):
    row_size = int(math.sqrt(len(matrix))) # =4 
    for i, num in enumerate(matrix): # Antalet element i matrix. i, num menas med att båda ska ++
        if num == target: # t.ex om 0 == 2 vilket dock inte hade uppfyllt
            row = i // row_size + 1
            col = i % row_size + 1
            print(f"{target} is at row {row} and column {col}")

Generate(), Generate()

# Function call to find the position of '2' in the matrix
find_position(Field, Field[RandomSquare])

# Bind the 'space' key to the space_key function
window.bind('<space>', space_key)
window.bind('<w>', w_key)

window.mainloop()