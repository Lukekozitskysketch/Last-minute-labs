# FILE NAME - while_loop_guess_high_low.py

# NAME: Luke Kozitsky
# DATE: 10-11-26
# BRIEF DESCRIPTION: number guess with feedback



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

scenarios = [
    [
        "Your guess is too low.",
        "Your guess is too high.",
        ""
    ],
    [
        ""
    ],
    [
        "Your guess is too low.",
        "Your guess is too low.",
        "Your guess is too low.",
        "Your guess is too high.",
        ""
    ]
]

for scenario in scenarios:
    for feedback in scenario:
        print("Guess a number: ")
        if feedback:
            print(feedback)
            print()
    print()
    tries = len(scenario)
    print(f"You guessed in {tries} tries.")








########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Guess a number: 22
Your guess is too low.

Guess a number: 44
Your guess is too high.

Guess a number: 33

You guessed in 3 tries.
'''


'''
Guess a number: 33

You guessed in 1 tries.
'''


'''
Guess a number: -9
Your guess is too low.

Guess a number: 100
Your guess is too high.

Guess a number: 30
Your guess is too low.

Guess a number: 32
Your guess is too low.

Guess a number: 34
Your guess is too high.

Guess a number: 33

You guessed in 6 tries.
'''

