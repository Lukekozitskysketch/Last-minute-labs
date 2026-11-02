import random

insults = [
    "You look like a bunch of rocks",
    "Your Ugly",
    "You smell",
    "Your nose looks weird",
    "Your socks are dirty",
    "You suck at python",
]


def welcome():
    print("---------------------------------")
    print("Welcome to the Insulternator 3500")
    print("---------------------------------")


def show_all_insults():
    print(insults)


def one_insult():
    print(random.choice(insults))


def two_insults():
    print(random.choice(insults))
    print(random.choice(insults))


def insult_specific_name(name=None):
    if name is None:
        name = input("What is your name? ")
    print(f"{name}, here is your insult: {random.choice(insults)}")


def insult_x_number_of_insults(num=None):
    if num is None:
        num = int(input("Enter number of insults: "))
    for _ in range(num):
        print(random.choice(insults))


def goodbye():
    print("---------------------------------------------")
    print("Thank you for playing the Insulternator 3500!")
    print("---------------------------------------------")
