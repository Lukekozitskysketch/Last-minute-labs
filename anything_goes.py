# FILE NAME - anything_goes.py
# Remember to cite any sources you used to help you complete this project!

# NAME: Luke Kozitsky
# DATE: 11-25-26
# BRIEF DESCRIPTION: This is a rock, paper, scissors game the first player to 10 will win
# I wrote the foundation of the code, and gemini helped me finish it off

import random

# this shows the 3 choices in my game and sets each score to 0
choices = ["rock", "paper", "scissors"]
round_history = []
player_score = 0
computer_score = 0


# loop runs until we have a winner
while player_score < 10 and computer_score < 10:
    # player input reduced to lowercase
    player = input("\nChoose rock, paper, or scissors: ").lower()

    # make sure the user entered a valid choice
    if player not in choices:
        print("Invalid choice, try again.")
        continueinue

    # computer picks a move
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # decide who won the round
    if player == computer:
        print("It's a tie!")
        round_history.append(f"Tie ({player} vs {computer})")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
        round_history.append(f"You won ({player} beats {computer})")
    else:
        print("Computer wins this round!")
        computer_score += 1
        round_history.append(f"Computer won ({computer} beats {player})")

    # shows the current score
    print(f"Score -> You: {player_score} | Computer: {computer_score}")

# decides who won 
if player_score == 10:
    result = "You won this game!"
else:
    result = "The Computer won this game!"

# this shows the final match to the screen
print("\n" + "=" * 35)
print(result)
print(f"Total Rounds Played: {len(round_history)}")
print("Match Recap:")
for i in range(len(round_history)):
    print(f"  Round {i + 1}: {round_history[i]}")
print("=" * 35)print("\n" + result)

# records the final score to a text file
with open("rps_results.txt", "w") as file:
    file.write(f"Final Score -> You: {player_score} | Computer: {computer_score}\n")
    file.write(result + "\n\n")
    file.write("Round-by-Round History:\n")
    for i in range(len(round_history)):
        file.write(f"  Round {i + 1}: {round_history[i]}\n")

########################################
#          REFLECTION QUESTIONS
########################################

'''
Remember to cite any sources you used to help you complete this project.
You can do that here in this section or cite as comments throughout your code.

1. How did you choose the goal of your program?
I picked it from the list of choices you gave

2. What part of this project challenged you the most? How did you work through that challenge?
Writing the conditionals for every winning combination without making the code messy was the hardest part.
I worked through it by grouping the three winning moves with 'or' statements and testing each round.

3. If you had 10 more hours to improve or expand your program, what would you change? Why?
I would let the player choose the winning score (like best of 3 or 5) and save a running 
win/loss history to the text file instead of overwriting it. So the player would have more control

'''
