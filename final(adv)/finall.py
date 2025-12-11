# Program Final.py
# Class: CSE 1321L
# Section: 1
# Term: 1
# Instructor: Rui Wu
# Name: Bryce Armand
# assignment: final
#convert coins in a sentence to dollar amount


def coin_values_list  (sentence):


    # Dictionary of coin in cents
    coin_values = {
        "penny": 1,
        "pennies": 1,
        "nickel": 5,
        "nickels": 5,
        "dime": 10,
        "dimes": 10,
        "quarter": 25,
        "quarters": 25
    }


    sentence = sentence.lower().strip()

    # Remove and
    sentence = sentence.replace("and", " ")

    # splits the words
    tokens = sentence.split()

    # removes puncuation
    cleaned_tokens = []
    for t in tokens:

        cleaned_tokens.append(t.strip(".,!?;:"))

    tokens = cleaned_tokens

    total_cents = 0

    # adds the number to the total
    i = 0
    while i < len(tokens) - 1:
        if tokens[i].isdigit():
            quantity = int(tokens[i])
            coin = tokens[i + 1]

            if coin in coin_values:
                total_cents += quantity * coin_values[coin]

        i += 1

    # conversion
    return total_cents / 100.0


def main():
    print("[Coin sentence to dollars ]")


    while True:
        print("example: mary has 300 nickels and 1000 pennies")
        user_input = input("Enter a sentence with coins in it (press 'q' to quit): ").strip()


        if user_input.lower() in ("q", "quit"):
            print("Goodbye!")
            break

        total_dollars = coin_values_list(user_input)
        print(f"Total dollar amount: {total_dollars:.2f}")


if __name__ == "__main__":
    main()
