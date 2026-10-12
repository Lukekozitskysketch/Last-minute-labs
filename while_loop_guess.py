# FILE NAME - while_loop_guess.py

# NAME: Luke Kozitsky
# DATE: 10-11-26
# BRIEF DESCRIPTION:  Guess a number statement in python



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

scenarios = [3, 6, 1]

for tries in scenarios:
    for _ in range(tries):
        print("Guess a number: ")
    print(f"You guessed in {tries} tries.")


########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Guess a number: 22
Guess a number: 44
Guess a number: 33
You guessed in 3 tries.
'''


'''
Guess a number: 33
You guessed in 1 tries.
'''


'''
Guess a number: -9
Guess a number: 100
Guess a number: 30
Guess a number: 32
Guess a number: 34
Guess a number: 33
You guessed in 6 tries.
'''

