# Program Name: Assignment3.py
# Course: IT3883/Section 1
# Student Name: Bryce Armand
# Assignment Number: Assignment 3
# Due Date: 10/3/2025
# Purpose: write a GuI that will conver miles per gallon into kilometers per liter
# I used the notes from in class to make the layout and used W3 to help find a way to change color
from tkinter import *


convert_fact = 0.425143707

# this creates the window
top = Tk()
top.geometry("500x300")
top.configure(bg="blue")
top.title("MPG to KM/L Converter")

# function that converts and updates
def convert(event):
    value = entry.get()
    if value == "":
        result["text"] = ""
    else:
        try:
            mpg = float(value)
            kpl = mpg * convert_fact
            result ["text"] = f"{kpl:.2f} km/l" # the number is rounded to 2 decimal places
        except ValueError:  # this was made not allow any letters
            result ["text"] = ""

# Instruction label
label = Label(top, text="Enter MPG:", font=("Arial", 14), bg="blue", fg="white")
label.pack(pady=10)

# box
entry = Entry(top, font=("Arial", 14))
entry.pack(pady=10)

# Result label
result = Label(top, text="", font=("Arial", 16, "bold"), bg="blue", fg="yellow")
result.pack(pady=20)

# (practice other ways to update the number)
entry.bind("<KeyRelease>", convert)

top.mainloop()