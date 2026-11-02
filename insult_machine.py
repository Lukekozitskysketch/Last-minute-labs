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
    line1 = "-" * 33
    line2 = "Welcome to the Insulternator 3500"
    line3 = "-" * 33
    print(line1)
    print(line2)
    print(line3)
    return f"{line1}\n{line2}\n{line3}"


def show_all_insults():
    print(insults)
    return str(insults)


def one_insult():
    res = random.choice(insults)
    print(res)
    return res


def two_insults():
    res1 = random.choice(insults)
    res2 = random.choice(insults)
    print(res1)
    print(res2)
    return f"{res1}\n{res2}"


def insult_specific_name(name=None):
    if name is None:
        name = input("What is your name? ")
    res = f"{name}, here is your insult: {random.choice(insults)}"
    print(res)
    return res


def insult_x_number_of_insults(num=None):
    if num is None:
        num = int(input("Enter number of insults: "))
    if num <= 0:
        return ""
    lines = [random.choice(insults) for _ in range(num)]
    for line in lines:
        print(line)
    return "\n".join(lines)


def goodbye():
    line1 = "-" * 45
    line2 = "Thank you for playing the Insulternator 3500!"
    line3 = "-" * 45
    print(line1)
    print(line2)
    print(line3)
    return f"{line1}\n{line2}\n{line3}"
