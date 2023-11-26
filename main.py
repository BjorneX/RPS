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



#Variables

Field = [0,0,0,0,
         0,0,0,0,
         0,0,0,0,
         0,0,0,0,]

# For  =0

RandomSquare = random.randint(0, len(Field) - 1)

Field[RandomSquare] = 2

#Visuals

def output():
    print("Press 'w' to display the field!\n")

    field_size = int(math.sqrt(len(Field)))

    for i in range(0, len(Field), field_size):
        for j in range(field_size):
            print(Field[i+j], end=' ')
        print()

def w_key(event):
    if event.name == 'w':
        output()

window.title("Press 'w' to Display Field")

# Bind 'w' key event to w_key function
keyboard.on_press_key('w', w_key)

window.mainloop()