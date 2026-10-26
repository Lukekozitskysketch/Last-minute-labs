# FILE NAME - average_values.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION: 




# Declare the list called `numbers`
numbers = []

# Keep running through this `while` loop forever
while True:

    # Prompt the user for a number (or "DONE" when finished)
    user_input = input('Enter a number ("DONE" to finish): ')
    
    # If the input is "DONE", break out of the `while`` loop
    if user_input == 'DONE':
        print('\n---END OF INPUT---\n')
        break
    else:
        # Otherwise, convert the input to an `int` and append
        # it to the list called `numbers`
        numbers.append(int(user_input))

#########################################
#               YOUR JOB:               #
#                                       #
# 1. Create a variable, `sum`, and set  #
#    it equal to 0.                     #
# 2. Iterate through the list and add   #
#    the value of each index to sum     #
# 3. Output the list, the sum, and the  #
#    average.                           #
#########################################

########## ENTER YER CODE BELOW THIS LINE ##########










########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''
Enter a number ("DONE" to finish): 1
Enter a number ("DONE" to finish): 2
Enter a number ("DONE" to finish): 3
Enter a number ("DONE" to finish): 4
Enter a number ("DONE" to finish): 5
Enter a number ("DONE" to finish): DONE

---END OF INPUT---

NUMBERS =  [1, 2, 3, 4, 5]
SUM = 15
AVERAGE =  3.0
'''


'''
Enter a number ("DONE" to finish): -1
Enter a number ("DONE" to finish): 1
Enter a number ("DONE" to finish): 2
Enter a number ("DONE" to finish): -2
Enter a number ("DONE" to finish): DONE

---END OF INPUT---

NUMBERS =  [-1, 1, 2, -2]
SUM = 0
AVERAGE =  0.0
'''


'''
Enter a number ("DONE" to finish): 1
Enter a number ("DONE" to finish): DONE

---END OF INPUT---

NUMBERS =  [1]
SUM = 1
AVERAGE =  1.0
'''




########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the hardest part of this lab?







'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[ ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''