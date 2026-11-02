
# FILE NAME - fortune_util.py
# AUTHOR - Dave Ghidiu
# DATE - October 3, 2022
# DESCRIPTION - A utility module for telling fortunes

import random

FORTUNES = [
    "There's a lot of atoms in you.",
    "Bring an umbrella today.",
    "You will live a long, prosperous life.",
    "Chin up! It's going to be a great day!",
    "If you have no pockets, your phone can't fall out of them!",
    "Fear is for chumps!"
]

def display_welcome():
    print("-" * 50)
    print("Welcome to the Fortune Telling Machine\n")
    print("The instructions are simple - you may request one")
    print("fortune, you may request multiple fortunes, or you")
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
        pass
########################################
#          SAMPLE OUTPUT
########################################

'''

--------------------------------------------------
Welcome to the Fortune Telling Machine

The instructions are simple - you may request one
fortune, you  may request multiple fortunes, or you
may request to quit.

Please enjoy your fortune(s)! But beware! When you use
the Fortune Telling Machine, you get what you get and
you don't get upset!

--------------------------------------------------
ONE FORTUNE:
There's a lot of atoms in you.


--------------------------------------------------
MULTIPLE FORTUNES:
How many fortunes would you like? 7

1 - Bring an umbrella today.

2 - There's a lot of atoms in you.

3 - You will live a long, prosperous life.

4 - Chin up! It's going to be a great day!

5 - If you have no pockets, your phone can't fall out of them!

6 - Chin up! It's going to be a great day!

7 - You will live a long, prosperous life.

--------------------------------------------------

I hope you enjoyed your fortunes...

'''
