import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while player_score < 10 and computer_score < 10:
    player = input("\nChoose rock, paper, or scissors: ").lower()
    if player not in choices:
        print("Invalid choice, try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}")

if player_score == 10:
    result = "You won the game!"
else:
    result = "Computer won the game!"

print("\n" + result)

with open("rps_results.txt", "w") as file:
    file.write(f"Final Score -> You: {player_score} | Computer: {computer_score}\n")
    file.write(result + "\n")
