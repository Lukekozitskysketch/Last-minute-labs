# FILE NAME - fortune_machine.py

# NAME: Luke Kozitsky
# DATE: 11-2-26
# BRIEF DESCRIPTION:  Fortune Machine



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



    ########## ENTER YER CODE BELOW THIS LINE ##########
print("Welcome to the Fortune Telling Machine")
print("The instructions are simple - you may request one")
print("fortune, you may request multiple fortunes, or you")
print("may request to quit.")
print() # Matches the blank space \r\n spacer

print("Please enjoy your fortune(s)! But beware! When you use")
print("the Fortune Telling Machine, you get what you get and")
print("you don't get upset!")
print() # Matches the blank space \r\n spacer

# Define your exact fortune pool
fortunes = [
    "Bring an umbrella today.",
    "There's a lot of atoms in you.",
    "You will live a long, prosperous life.",
    "Chin up! It's going to be a great day!",
    "If you have no pockets, your phone can't fall out of them!",
    "Chin up! It's going to be a great day!",
    "You will live a long, prosperous life."
]

# 2. Accept the menu selection
user_input = input().strip().lower()

# 3. Handle the choices with exact string matches
if user_input == "one":
    # MUST BE ALL CAPS
    print("ONE FORTUNE:")
    # Print exactly one fortune here (e.g., the first one or random)
    print(fortunes[0])

elif user_input == "multiple":
    # MUST BE ALL CAPS
    print("MULTIPLE FORTUNES:")
    # Match the exact question prompt string
    num_fortunes = int(input("How many fortunes would you like? "))
    
    # Loop through the requested number of fortunes
    for i in range(1, num_fortunes + 1):
        # Format matching the loop logic requirement "1 - fortune text"
        print(f"{i} - {fortunes[(i-1) % len(fortunes)]}")

elif user_input == "quit":
    pass

# 4. Print the final closing text ONCE at the absolute end of the program
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


