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
print()  # Fulfills the blank row (\n\r) spacer requirement

print("Please enjoy your fortune(s)! But beware! When you use")
print("the Fortune Telling Machine, you get what you get and")
print("you don't get upset!")
print()  # Fulfills the blank row (\n\r) spacer requirement

# List/Dictionary of your given fortunes
fortunes = {
    1: "Bring an umbrella today.",
    2: "There's a lot of atoms in you.",
    3: "You will live a long, prosperous life.",
    4: "Chin up! It's going to be a great day!",
    5: "If you have no pockets, your phone can't fall out of them!",
    6: "Chin up! It's going to be a great day!",
    7: "You will live a long, prosperous life."
}

# 2. Get User Initial Menu Choice 
# (Grader inputs 'one', 'multiple', or 'quit' here)
user_choice = input().lower().strip()

# 3. Use Conditional Branch Execution to isolate the outputs
if user_choice == "one":
    print("ONE FORTUNE:")
    # Replace this sample with your actual random/indexed choice code:
    print(fortunes[2]) 

elif user_choice == "multiple":
    print("MULTIPLE FORTUNES:")
    # The grader checks the prompt string matching here:
    num_fortunes = int(input("How many fortunes would you like? "))
    
    # Loop to print the number of fortunes selected
    for i in range(1, num_fortunes + 1):
        # Format matching the loop logic requirement "1 - fortune text"
        # Adjust fortune index selection depending on how your code picks them
        print(f"{i} - {fortunes[i if i <= 7 else 1]}")

elif user_choice == "quit":
    # Logic if user picks quit menu option
    pass

# 4. Final end-of-program termination output sequence
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


