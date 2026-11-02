import random

FORTUNES = [
    "There's a lot of atoms in you.",
    "Bring an umbrella today.",
    "You will live a long, prosperous life.",
    "Chin up! It's going to be a great day!",
    "If you have no pockets, your phone can't fall out of them!",
    "Fear is for chumps!"
]

def main():
    run_fortune_machine()

def run_fortune_machine():

    ########## ENTER YER CODE BELOW THIS LINE ##########
    print("-" * 50)
    print("Welcome to the Fortune Telling Machine\n")
    print("The instructions are simple - you may request one")
    print("fortune, you  may request multiple fortunes, or you")
    print("may request to quit.\n")
    print("Please enjoy your fortune(s)! But beware! When you use")
    print("the Fortune Telling Machine, you get what you get and")
    print("you don't get upset!")
    print("-" * 50)

    print("ONE FORTUNE:")
    print(random.choice(FORTUNES))
    print("\n")

    print("-" * 50)
    print("MULTIPLE FORTUNES:")
    try:
        count = int(input("How many fortunes would you like? "))
        print()
        for i in range(1, count + 1):
            print(f"{i} - {random.choice(FORTUNES)}\n")
    except ValueError:
        pass

    print("-" * 50)
    print("\nI hope you enjoyed your fortunes...")
    ########### END YER CODE ABOVE THIS LINE ###########


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


