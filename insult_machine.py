import random
import sys
import types

insults = [
    "You look like a bunch of rocks",
    "Your Ugly",
    "You smell",
    "Your nose looks weird",
    "Your socks are dirty",
    "You suck at python",
]


def welcome():
    lines = [
        "---------------------------------",
        "Welcome to the Insulternator 3500",
        "---------------------------------",
    ]
    for line in lines:
        print(line)
    return lines


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
    return [res1, res2]


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
        return []
    lines = []
    for _ in range(num):
        res = random.choice(insults)
        print(res)
        lines.append(res)
    return lines


def goodbye():
    lines = [
        "---------------------------------------------",
        "Thank you for playing the Insulternator 3500!",
        "---------------------------------------------",
    ]
    for line in lines:
        print(line)
    return lines


funcs = {
    "insults": insults,
    "welcome": welcome,
    "show_all_insults": show_all_insults,
    "one_insult": one_insult,
    "two_insults": two_insults,
    "insult_specific_name": insult_specific_name,
    "insult_x_number_of_insults": insult_x_number_of_insults,
    "goodbye": goodbye,
}

if "insult_machine_util" not in sys.modules:
    mod = types.ModuleType("insult_machine_util")
    sys.modules["insult_machine_util"] = mod

target = sys.modules["insult_machine_util"]
for name, func in funcs.items():
    setattr(target, name, func)
