# Goal: To guess the computers secret number
import random
wrong_messages = ["Nope!", "Not quite!", "Keep trying!", "Almost!", "Hmm, no!"]
name = input("What's your name? ")
print(f"Welcome, {name}! I'm thinking of a number between 1 and 20.")

secret = random.randint(1, 20)
tries = 0
#This is where Claude takes over. I gave it the goal and some things to get it started
while True:
    guess = int(input("Your guess: "))
    tries = tries + 1

    if guess < secret:
        print(f"{random.choice(wrong_messages)} Too low.")
    elif guess > secret:
        print(f"{random.choice(wrong_messages)} Too high.")
    else:
        print(f"You got it, {name}! The number was {secret}.")
        print(f"It took you {tries} tries.")
        break

# Give a rating based on how many tries it took
if tries <= 3:
    print("Amazing! You're a mind reader!")
elif tries <= 6:
    print("Nice job!")
else:
    print("You got there in the end!")
