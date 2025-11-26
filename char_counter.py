# Developed by: Nathan Miller                                             # ----------------------------------------- #
# Created: November 18, 2020                                              # ----------[ mostLettersNM.py ]----------- #
# ------- Objective of assignment: -------------------------------------- # ----------------------------------------- #
# - Gather and display string from user input                             # Psuedo-Structure:                         #
# - count each character in the string                                    #               [comments]                  #
# - determine most common character                                       #               get_string()                #
# -------- Questions: --------------------------------------------------- #               print_string()              #
# - Uppercase vs Lowercase = same or different?                           #               count_string()              #
# - Should the program exclude spaces?                                    #               end()                       #
# - Solution: Made optional for user                                      #               main()                      #
# ----------------------------------------------------------------------- # ----------------------------------------- #
import random


def config(string):  # This function grants user optional configs for case sensitivity and spaces
    while True:
        option = input("\nHow would you like the program to handle case sensitivity, and spaces?\n"
                       "1 - Case sensitive, include spaces in count\n"
                       "2 - Case sensitive, omit spaces from the count\n"
                       "3 - Case insensitive, include spaces in count\n"
                       "4 - Case insensitive, omit spaces from the count\n")
        if option == "1":
            print("Provided text: '" + string + "'")
            return string
        elif option == "2":
            text = string.replace(" ", "")
            print("Provided text: '" + string + "'\n"
                  "Modified text: '" + text + "'")
            return text
        elif option == "3":
            text = string.upper()
            print("Provided text: '" + string + "'\n"
                  "Modified text: '" + text + "'")
            return text
        elif option == "4":
            text = string.upper().replace(" ", "")
            print("Provided text: '" + string + "'\n"
                  "Modified text: '" + text + "'")
            return text
        else:
            print("I'm not quite sure what you meant by '" + option + "' Please, try again!")


def get_string():  # This function gathers input from user to create a string
    random_letters = ""  # <-- a blank string to concatenate random letters to
    random_fruits = ""  # <-- a blank string to concatenate random fruits to
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"  # sample key for random characters
    fruits = ["Pomegranate", "Apple", "Banana", "Orange", "Pear", "Pineapple", "Guava", "Kiwi", "Mango", "Peach",
              "Plum", "Lime", "Lemon", "Watermelon", "Strawberry", "Grape", "Cherry", "Papaya", "Coconut", "Avocado",
              "Starfruit", "Cantaloupe", "Blueberry", "Raspberry", "Cranberry", "Grapefruit", "Passion Fruit"]
    for i in range(100):  # Random letters
        rnd_letter = random.choice(sample)
        random_letters += rnd_letter
    for i in range(15):  # Random fruits
        b = random.randrange(0, len(fruits))
        random_fruits += fruits[b] + " "
        if i == 14:
            random_fruits = random_fruits.rstrip(" ")
    while True:  # Ask user if they'd like to type manually, or have string randomly created
        answer = input("Would you like to type out a string manually, or have one generated for you?\n"
                       "1 - Enter a string manually. \n"
                       "2 - Randomly generate a string. \n")
        if answer == "1":
            user_input = input("Tell me anything: ")
            text = user_input
            text = config(text)
            return text
        elif answer == "2":
            while True:
                answer = input("How would you like the program to randomly generate your string?\n"
                               "1 - Random Fruits\n"
                               "2 - Random Letters\n")
                if answer == "1":
                    text = random_fruits
                    text = config(text)
                    return text
                elif answer == "2":
                    text = random_letters
                    text = config(text)
                    return text
                else:
                    print("I'm not quite sure what you mean by '" + answer + "' Please, try again!")
        else:
            print("I'm not quite sure what you mean by '" + answer + "' Please, try again!")


def print_count(range_val, tup_list, string):  # This function takes a number for range, list of tuples, and a string
    try:                                       # as arguments, and prints the results range_val times.
        for i in range(range_val):
            char = tup_list[i][1]
            num = tup_list[i][0]
            if len(tup_list) > 0:
                perc = round((num / len(string) * 100), 2)
            else:
                perc = 0
            print(str(i + 1) + ". '" + char + "' appears", num, "times, and makes up " + str(perc) + "% of the string.")
    except IndexError:  # In the case of a user entering a world with less than 3 unique characters, IndexError occurs.
        if len(tup_list) > 1:
            print("Only", len(tup_list), "unique characters? That's not very exciting.")
        elif len(tup_list) == 1:
            print("Only 1 unique character? That's not very exciting.")
        else:
            print("Really? There's nothing here!")


def count_string():
    tuples = []  # Blank list to append tuples to.
    text = get_string()  # text is returned from get_string function based on user's input.

    for char in set(text):  # This for loop iterates once per unique character in string.
        counter = text.count(char)  # This line counts occurrences of char in the string 'text'
        tup = counter, char  # <-- Tuple of occurrences in string, and the current character in index
        tuples.append(tup)

    tuples = sorted(tuples, reverse=True)  # List reversed so it is in order from greatest to least.
    print("\nBelow are the top 3 most occurring characters in the string:")
    print_count(3, tuples, text)

    view_full = input("\nWould you like to view the full list of all character counts in the string? (Y/N): ").upper()
    if view_full == "Y":
        print_count(len(tuples), tuples, text)


def end():  # This function allows user to restart or end program.
    while True:
        restart = input("\nWould you like to restart the program? (Y/N): ")
        if restart.upper() == 'Y':
            print("Input received:", restart)
            print("\nProgram is restarting...\n")
            run = True
            return run
        elif restart.upper() == 'N':
            print("Input received:", restart)
            print("\nProgram is terminating...\n")
            adios = input("Press 'ENTER' to exit program...")
            print("Input received: '" + adios + "'\nGoodbye!")
            run = False
            return run
        else:
            print("I'm not sure what you meant by '" + restart + "'. Please, try again.")


def main():
    print("\nWelcome to the Character Counter! I can count the characters in any string provided to me.\n")
    run = True  # Signal run loop to begin
    while run:  # Run loop
        count_string()
        run = end()  # run either stays True, or becomes False


main()
