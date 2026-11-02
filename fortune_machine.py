import random

FORTUNES = [
    "There's a lot of atoms in you.",
    "Bring an umbrella today.",
    "You will live a long, prosperous life.",
    "Chin up! It's going to be a great day!",
    "If you have no pockets, your phone can't fall out of them!",
    "Fear is for chumps!"
]

def print_welcome():
    print("-" * 50)
    print("Welcome to the Fortune Telling Machine\n")
    print("The instructions are simple - you may request one")
    print("fortune, you  may request multiple fortunes, or you")
    print("may request to quit.\n")
    print("Please enjoy your fortune(s)! But beware! When you use")
    print("the Fortune Telling Machine, you get what you get and")
    print("you don't get upset!")
    print("-" * 50)

def get_one_fortune():
    print("ONE FORTUNE:")
    print(random.choice(FORTUNES))
    print()

def get_multiple_fortunes():
    print("MULTIPLE FORTUNES:")
    try:
        count = int(input("How many fortunes would you like? "))
        print()
        for i in range(1, count + 1):
            print(f"{i} - {random.choice(FORTUNES)}\n")
    except ValueError:
        print("Please enter a valid number next time!\n")

def main():
    while True:
        print_welcome()
        print("Options:")
        print("1. One Fortune")
        print("2. Multiple Fortunes")
        print("3. Quit")
        choice = input("What would you like to do? (1/2/3): ").strip()
        print()
        if choice == "1":
            print("-" * 50)
            get_one_fortune()
            print("-" * 50)
            print("\nI hope you enjoyed your fortunes...\n")
        elif choice == "2":
            print("-" * 50)
            get_multiple_fortunes()
            print("-" * 50)
            print("\nI hope you enjoyed your fortunes...\n")
        elif choice == "3" or choice.lower() == 'quit':
            print("Goodbye! May good fortune follow you.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 


getting all the fortunes to process



2. What value do you see in having external modules?
Its saves time and extra work





'''


