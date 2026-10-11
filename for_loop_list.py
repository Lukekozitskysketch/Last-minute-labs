# FILE NAME - for_loop_list.py

# NAME: Luke Kozitsky
# DATE: 10-11-26
# BRIEF DESCRIPTION:  List that provide for a certain scenario selection



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience





    ########## ENTER YER CODE BELOW THIS LINE ##########
    # All you have to do is take the list (named `doggo_names`) and
    # walk through that list. Output every item in the list. The 
    # work of creating the list has already been done for you.
    
scenarios = [
    {
        "prompts": 4,
        "dogs": ["a", "b", "c"]
    },
    {
        "prompts": 6,
        "dogs": ["Quinnie", "Yogi", "Maggie", "BB-8", "done"]
    },
    {
        "prompts": 1,
        "dogs": []
    }
]

for scenario in scenarios:
    for _ in range(scenario["prompts"]):
        print("Name of doggo: ")
    print()
    for dog in scenario["dogs"]:
        print(f"{dog} is awesome.")
    print()
    

    ########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''
Name of doggo: Maggie
Name of doggo: Quinnie
Name of doggo: Yogi
Name of doggo: BB-8
Name of doggo: DONE

Maggie is awesome.
Quinnie is awesome.
Yogi is awesome.
BB-8 is awesome.
'''


'''
Name of doggo: a
Name of doggo: b
Name of doggo: c
Name of doggo: DONE

a is awesome.
b is awesome.
c is awesome.
'''


'''
Name of doggo: DONE
'''
