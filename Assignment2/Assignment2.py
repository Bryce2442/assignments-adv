# Program Name: Assignment2.py
# Course: IT3883/Section 1
# Student Name: Bryce Armand
# Assignment Number: 2
# Due Date: 9/19/2025
# Purpose: to make a program that will take input data from a file and give an output.

def calculate_average(grades):
    return sum(grades) / len(grades)


# opens the file
with open("Assignment2input.txt", "r") as file:
    students = []

    # reads the file
    for line in file:
        parts = line.strip().split()  # to split
        name = parts[0]  # first part is the students names
        grades = list(map(int, parts[1:]))  # Convert remaining fields to integers
        stu_average = calculate_average(grades)  # average
        students.append((name, stu_average))

# Sort the students list by average in descending order (used chat to find how to sort the students)
students.sort(key=lambda x: x[1], reverse=True)

# added the print and with 2 decimals at the end
for student in students:
    print(f"{student[0]} {student[1]:.2f}")