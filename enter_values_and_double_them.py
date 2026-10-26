# FILE NAME - double_values.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION: 

   


# First, let's figure out how many numbers the user will be entering:
size = int(input('How many numbers will you be entering? '))

# Next let's make a list. It's OK if the list doesn't have a length
# yet as we will just be appending to it.
numbers = []
double_numbers = []

# Guess we'll need a loop to populate the loop:
while len(numbers) < size:

    # Here's the tricky part. Stay with me! We have to ask the user to
    # input a number using the `input` function. Then we have to cast
    # it to an `int` before we append it. Otherwise, the list `numbers`
    # will be full of `strings`!
    num = int(input('What is number? '))
    numbers.append(num)


# Empty line for visual break
print()

##########################################
#               YOUR JOB:                #
#                                        #
# 1. Print out the list naturally        #
# 2. Sort the list                       #
# 3. Print out the sorted list naturally #
# 4. Print out the list with each        #
#    element doubled                     #
#                                        #
#########################################

########## ENTER YER CODE BELOW THIS LINE ##########

# HINT: It might be easier to create a second list








########### END YER CODE ABOVE THIS LINE ###########    





########################################
#          SAMPLE OUTPUT
########################################

'''
How many numbers will you be entering? 5
What is number? 1
What is number? 9
What is number? 2
What is number? 8
What is number? 7

ORIGINAL -          [1, 9, 2, 8, 7]
ORIGINAL (sorted) - [1, 2, 7, 8, 9]
DOUBLED -           [2, 4, 14, 16, 18]
'''


'''
How many numbers will you be entering? 0

ORIGINAL -          []
ORIGINAL (sorted) - []
DOUBLED -           []
'''


'''
How many numbers will you be entering? 1
What is number? 3

ORIGINAL -          [3]
ORIGINAL (sorted) - [3]
DOUBLED -           [6]
'''


'''
How many numbers will you be entering? 9
What is number? 193
What is number? 265
What is number? 295
What is number? -54
What is number? -523 
What is number? 463
What is number? 574
What is number? 2  
What is number? 0

ORIGINAL -          [193, 265, 295, -54, -523, 463, 574, 2, 0]
ORIGINAL (sorted) - [-523, -54, 0, 2, 193, 265, 295, 463, 574]
DOUBLED -           [-1046, -108, 0, 4, 386, 530, 590, 926, 1148]
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. How did you solve the problem of doubling the values?







'''



########################################
#            ATTESTATION
########################################

'''


It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''