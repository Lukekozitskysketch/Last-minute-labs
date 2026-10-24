# FILE NAME - sort_values_and_output.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience





# Declare the variable 'name' and give it a value of NONE
name = None

# Declare the list 'names' but keep it empty
names = []

# Here we populate the list. We will keep appending input from the user
# to the list unless the input is '_DONE_'. Note the tricky part - we 
# have to make sure we don't append '_DONE_' to the list!
while (name != '_DONE_'):
    name = input('Enter a name (enter "_DONE_" to end): ')
    if name == '_DONE_':
        break
    else:
        names.append(name)

# Empty line for visual break
print()

#########################################
#               YOUR JOB:               #
#                                       #
# 1. Print out the list naturally       #
# 2. Sort the list                      #
# 3. Print out the list naturally       #
# 4. Reverse the list                   #
# 5. Print out the list naturally       #    
#                                       #
#########################################



########## ENTER YER CODE BELOW THIS LINE ##########










########### END YER CODE ABOVE THIS LINE ###########







########################################
#          SAMPLE OUTPUT
########################################

'''
Enter a name (enter "_DONE_" to end): JD
Enter a name (enter "_DONE_" to end): Elliot
Enter a name (enter "_DONE_" to end): Turk
Enter a name (enter "_DONE_" to end): Dr. Kelso
Enter a name (enter "_DONE_" to end): Dr. Cox
Enter a name (enter "_DONE_" to end): Carla
Enter a name (enter "_DONE_" to end): Janitor
Enter a name (enter "_DONE_" to end): Ted
Enter a name (enter "_DONE_" to end): _DONE_

ORIGINAL - ['JD', 'Elliot', 'Turk', 'Dr. Kelso', 'Dr. Cox', 'Carla', 'Janitor', 'Ted']
SORTED - ['Carla', 'Dr. Cox', 'Dr. Kelso', 'Elliot', 'JD', 'Janitor', 'Ted', 'Turk']
REVERSED - ['Turk', 'Ted', 'Janitor', 'JD', 'Elliot', 'Dr. Kelso', 'Dr. Cox', 'Carla']
'''


'''
Enter a name (enter "_DONE_" to end): 1
Enter a name (enter "_DONE_" to end): 4
Enter a name (enter "_DONE_" to end): 10
Enter a name (enter "_DONE_" to end): 44
Enter a name (enter "_DONE_" to end): 50
Enter a name (enter "_DONE_" to end): _DONE_

ORIGINAL - ['1', '4', '10', '44', '50']
SORTED - ['1', '10', '4', '44', '50']
REVERSED - ['50', '44', '4', '10', '1'] 
'''


'''
Enter a name (enter "_DONE_" to end): Barney
Enter a name (enter "_DONE_" to end): Robin
Enter a name (enter "_DONE_" to end): Ted
Enter a name (enter "_DONE_" to end): Lily
Enter a name (enter "_DONE_" to end): Marshall
Enter a name (enter "_DONE_" to end): Victoria
Enter a name (enter "_DONE_" to end): Zoey
Enter a name (enter "_DONE_" to end): Stella
Enter a name (enter "_DONE_" to end): Scooter
Enter a name (enter "_DONE_" to end): James Van Der Beek
Enter a name (enter "_DONE_" to end): _DONE_

ORIGINAL - ['Barney', 'Robin', 'Ted', 'Lily', 'Marshall', 'Victoria', 'Zoey', 'Stella', 'Scooter', 'James Van Der Beek']
SORTED - ['Barney', 'James Van Der Beek', 'Lily', 'Marshall', 'Robin', 'Scooter', 'Stella', 'Ted', 'Victoria', 'Zoey']
REVERSED - ['Zoey', 'Victoria', 'Ted', 'Stella', 'Scooter', 'Robin', 'Marshall', 'Lily', 'James Van Der Beek', 'Barney']
'''


'''
Enter a name (enter "_DONE_" to end): alpha
Enter a name (enter "_DONE_" to end): BRAVO
Enter a name (enter "_DONE_" to end): delta
Enter a name (enter "_DONE_" to end): ECHO
Enter a name (enter "_DONE_" to end): CHARLIE
Enter a name (enter "_DONE_" to end): foxtrot
Enter a name (enter "_DONE_" to end): _DONE_

ORIGINAL - ['alpha', 'BRAVO', 'delta', 'ECHO', 'CHARLIE', 'foxtrot']
SORTED - ['BRAVO', 'CHARLIE', 'ECHO', 'alpha', 'delta', 'foxtrot']
REVERSED - ['foxtrot', 'delta', 'alpha', 'ECHO', 'CHARLIE', 'BRAVO']
'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?







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