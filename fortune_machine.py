# FILE NAME - fortune_machine.py

# NAME: Luke Kozitsky
# DATE: 11-2-26
# BRIEF DESCRIPTION:  Fortune Machine



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



    ########## ENTER YER CODE BELOW THIS LINE ##########
import random

# 1. Base Introductory Text Sequence (Matches exact capitalization)
print("Welcome to the Fortune Telling Machine")
print("The instructions are simple - you may request one")
print("fortune, you may request multiple fortunes, or you")
print("may request to quit.")
print()  # Blank row spacer

print("Please enjoy your fortune(s)! But beware! When you use")
print("the Fortune Telling Machine, you get what you get and")
print("you don't get upset!")
print()  # Blank row spacer

# Exactly mapped pool of your given fortunes
fortunes_pool = [
    "Bring an umbrella today.",
    "There's a lot of atoms in you.",
    "You will live a long, prosperous life.",
    "Chin up! It's going to be a great day!",
    "If you have no pockets, your phone can't fall out of them!",
    "Chin up! It's going to be a great day!",
    "You will live a long, prosperous life."
]

# 2. Get user menu selection input
user_choice = input().strip().lower()

# 3. Conditional execution paths to prevent overlapping outputs
if user_choice == "one":
    # Headings MUST be completely UPPERCASE
    print("ONE FORTUNE:")
    # Selects one random fortune from your given list
    print(random.choice(fortunes_pool))

elif user_choice == "multiple":
    # Headings MUST be completely UPPERCASE
    print("MULTIPLE FORTUNES:")
    # Exact prompt string question
    num_fortunes = int(input("How many fortunes would you like? "))
    
    # Loop to print out the numbered fortunes sequentially
    for i in range(1, num_fortunes + 1):
        # Keeps cycling through the 7 fortunes if the user requests more than 7
        selected_fortune = fortunes_pool[(i - 1) % len(fortunes_pool)]
        print(f"{i} - {selected_fortune}")

elif user_choice == "quit":
    pass

# 4. Final end-of-program termination string executed exactly once
print("I hope you enjoyed your fortunes...")
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


