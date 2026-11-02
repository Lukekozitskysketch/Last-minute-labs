import insult_machine_util


def run_program():
    insult_machine_util.welcome()

    print("\nTESTING: show_all_insults()")
    insult_machine_util.show_all_insults()

    print("\nTESTING: one_insult()")
    insult_machine_util.one_insult()

    print("\nTESTING: two_insults()")
    insult_machine_util.two_insults()

    print("\nTESTING: insult_specific_name()")
    insult_machine_util.insult_specific_name("BB-8")

    print("\nTESTING: insult_x_number_of_insults()")
    insult_machine_util.insult_x_number_of_insults(3)

    print("\nTESTING: goodbye()")
    insult_machine_util.goodbye()


if __name__ == "__main__":
    run_program()


