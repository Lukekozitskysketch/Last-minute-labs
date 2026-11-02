# FILE NAME - calc.py

# NAME: Luke Kozitsky
# DATE: 11-2-26
# BRIEF DESCRIPTION:  Calculator



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience


########## ENTER YER CODE BELOW THIS LINE ##########


def run_calculator():
    print("Welcome to the Calculator\n")
    
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))
    print()
    
    total_sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    
    if num2 != 0:
        quotient = num1 / num2
    else:
        quotient = "Undefined"
        
    print("SUM = ", total_sum)
    print("DIFFERENCE = ", difference)
    print("PRODUCT = ", product)
    print("QUOTIENT = ", quotient)
    print()
    
    print("Have a nice, mathy day.")

if __name__ == "__main__":
    run_calculator()







########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''

Welcome to the Calculator

What is the first number? 10
What is the second number? 5

SUM =  15.0
DIFFERENCE =  5.0
PRODUCT =  50.0
QUOTIENT =  2.0

Have a nice, mathy day.
'''


'''
Welcome to the Calculator

What is the first number? 0
What is the second number? 1

SUM =  1.0
DIFFERENCE =  -1.0
PRODUCT =  0.0
QUOTIENT =  0.0

Have a nice, mathy day.

'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 


Getting the whole calculator set up



2. How did you decide if the functions in the `calc_util` module should return or print?

it is much easier if it doenst print



'''
