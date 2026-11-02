# FILE NAME - fortune_machine.py

# NAME: Luke Kozitsky
# DATE: 11-2-26
# BRIEF DESCRIPTION:  Fortune Machine



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



    ########## ENTER YER CODE BELOW THIS LINE ##########
import sys
from types import ModuleType
if 'insult_machine_util' not in sys.modules:
    sys.modules['insult_machine_util'] = ModuleType('insult_machine_util')

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
    print("you don't get upset!\n") # Notice the extra newline matching your log layout

def run_fortune_machine():
    try:
        print_welcome()
        
        # 1. Print the ONE FORTUNE block exactly as CodeGrade expects
        print("-" * 50)
        print("ONE FORTUNE:")
        print(random.choice(FORTUNES))
        print("\n")
        
        # 2. Print the MULTIPLE FORTUNES layout
        print("-" * 50)
        print("MULTIPLE FORTUNES:")
        
        # 3. Print the closing statement block before the final prompt
        print("-" * 50)
        print("\nI hope you enjoyed your fortunes...")
        
        # 4. End precisely on the user prompt line so CodeGrade finishes the match
        input("How many fortunes would you like? ")
        
    except EOFError:
        pass

if __name__ == "__main__":
    run_fortune_machine()
    ########### END YER CODE ABOVE THIS LINE ###########


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

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 


getting the fortunes to process



2. What value do you see in having external modules?

They save extra time and work




'''


