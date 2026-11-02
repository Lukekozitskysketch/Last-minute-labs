import random

INSULTS = ["A", "B", "C", "D", "E", "F"]


def welcome():
    print("-" * 33)
    print("Welcome to the Insulternator 3500")
    print("-" * 33)


def show_all_insults():
    print(INSULTS)


def one_insult():
    print(random.choice(INSULTS))


def two_insults():
    print(random.choice(INSULTS))
    print(random.choice(INSULTS))


def insult_specific_name(name=None):
    if name is None:
        name = input("What is your name? ")
    print(f"{name}, here is your insult: {random.choice(INSULTS)}")


def insult_x_number_of_insults(num=None):
    if num is None:
        num = int(input("Enter number of insults: "))
    for _ in range(num):
        print(random.choice(INSULTS))


def goodbye():
    print("-" * 45)
    print("Thank you for playing the Insulternator 3500!")
    print("-" * 45)





if __name__ == "__main__":
    main()
