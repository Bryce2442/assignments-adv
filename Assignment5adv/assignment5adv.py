# Assignment5.py
# Class: IT3883
# Section: 1
# Term: 1
# Instructor: Rui Wu
# Name: Bryce Armand
# assignment: 5
#implementing sql into python and getting avg temps for sunday and thursday


import sqlite3

def main():
    # create or open the database
    conn = sqlite3.connect("temps.db")
    cur = conn.cursor()

    # this makes the table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS temps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_of_week TEXT,
            temperature_value REAL
        )
    """)

    # open's the file
    file = open("Assignment5input.txt", "r")

    # inserts data
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split()
        day = parts[0]
        temp = float(parts[1])
        cur.execute("INSERT INTO temps(day_of_week, temperature_value) VALUES (?, ?)", (day, temp))

    file.close()
    conn.commit()

    # average temperature for Sunday
    cur.execute("SELECT AVG(temperature_value) FROM temps WHERE day_of_week = 'Sunday'")
    sunday_avg = cur.fetchone()[0]

    # average temperature for Thursday
    cur.execute("SELECT AVG(temperature_value) FROM temps WHERE day_of_week = 'Thursday'")
    thursday_avg = cur.fetchone()[0]

    print("Average temperature for Sunday:", sunday_avg)
    print("Average temperature for Thursday:", thursday_avg)

    conn.close()

if __name__ == "__main__":
    main()