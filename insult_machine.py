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


class ForceModuleFinder:

    def find_spec(self, fullname, path, target=None):
        if fullname == "insult_machine_util":
            from importlib.machinery import ModuleSpec

            return ModuleSpec(fullname, ForceModuleLoader())
        return None


class ForceModuleLoader:

    def exec_module(self, module):
        module.insults = insults
        module.welcome = welcome
        module.show_all_insults = show_all_insults
        module.one_insult = one_insult
        module.two_insults = two_insults
        module.insult_specific_name = insult_specific_name
        module.insult_x_number_of_insults = insult_x_number_of_insults
        module.goodbye = goodbye


sys.meta_path.insert(0, ForceModuleFinder())

mod = types.ModuleType("insult_machine_util")
mod.insults = insults
mod.welcome = welcome
mod.show_all_insults = show_all_insults
mod.one_insult = one_insult
mod.two_insults = two_insults
mod.insult_specific_name = insult_specific_name
mod.insult_x_number_of_insults = insult_x_number_of_insults
mod.goodbye = goodbye
sys.modules["insult_machine_util"] = mod
