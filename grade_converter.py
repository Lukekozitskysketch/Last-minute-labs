# FILE NAME - grade_converter.py

# NAME: Luke Kozitsky
# DATE: 10-5-26
# BRIEF DESCRIPTION:  Python grade converter



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

import sys

def convert_grade():
    print("===== Grade Converter =====")
    try:
        val = input("Enter a numerical grade (1-100): ")
        score = int(val)
        
        if score > 100:
            grade = "A+"
        elif score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 65:
            grade = "D"
        else:
            grade = "F"
            
        print(grade)
        
    except (ValueError, EOFError):
        print("F")

if __name__ == "__main__":
    convert_grade()
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

To not foget to print the grade





'''
