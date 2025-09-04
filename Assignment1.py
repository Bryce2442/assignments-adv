# Program Name: Assignment1.py
# Course: IT3883/Section 1
# Student Name: Bryce Armand
# Assignment Number: Lab#
# Due Date: 9/5/ 2025
# Purpose: To make a menu that will loop and continusly add or clear buffers until it is turned off by a user input.
# List Specific resources used to complete the assignment. while loop, if, else.

choice = ""
buffer = ""

while choice != "4":
    #loops the program until 4 is chosen
    print("\nMenu:")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    choice = input("Enter your choice (1-4): ").strip()
#entering choice
    if choice == "1":
        data = input("Enter a string to append: ").strip()  # appends then prints that the data was appended
        buffer += data
        print("Data appended.")
    elif choice == "2":
        buffer = ""  #if 2 is selected buffer gets cleared
        print("Buffer cleared.")
    elif choice == "3":
        print("Current buffer:", buffer) # prints the current buffer
    elif choice != "4":
        print("Invalid choice. Please enter 1-4.") # end of the loop

print("Exiting program.")
