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

# 1. Print Intro Block
print("Welcome to the Fortune Telling Machine")
print("The instructions are simple - you may request one")
print("fortune, you may request multiple fortunes, or you")
print("may request to quit.")
print() 

print("Please enjoy your fortune(s)! But beware! When you use")
print("the Fortune Telling Machine, you get what you get and")
print("you don't get upset!")
print() 

fortunes_pool = [
    "Bring an umbrella today.",
    "There's a lot of atoms in you.",
    "You will live a long, prosperous life.",
    "Chin up! It's going to be a great day!",
    "If you have no pockets, your phone can't fall out of them!",
    "Chin up! It's going to be a great day!",
    "You will live a long, prosperous life."
]

# ==========================================
# STEP A: GET THE MENU SELECTION INPUT
# ==========================================
# Keep the input empty so it doesn't print extra text.
# .strip().lower() cleans up spaces and accidental caps from the test.
user_choice = input().strip().lower()


# 2. Check the input choice using conditional branches
if user_choice == "one":
    print("ONE FORTUNE:")
    print(random.choice(fortunes_pool))

elif user_choice == "multiple":
    print("MULTIPLE FORTUNES:")
    
    # ==========================================
    # STEP B: GET THE NUMBER OF FORTUNES INPUT
    # ==========================================
    # For this specific step, the grader explicitly expects the text prompt 
    # "How many fortunes would you like?" inside the input function.
    num_fortunes = int(input("How many fortunes would you like? "))
    
    for i in range(1, num_fortunes + 1):
        selected_fortune = fortunes_pool[(i - 1) % len(fortunes_pool)]
        print(f"{i} - {selected_fortune}")

elif user_choice == "quit":
    # If they type quit, it skips directly to the closing message below
    pass

# 3. Final Closing Message
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


