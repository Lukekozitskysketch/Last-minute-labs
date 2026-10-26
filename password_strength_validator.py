# FILE NAME - password_strength_analyzer.py

# NAME: Luke Kozitsky
# DATE: 10-26-26
# BRIEF DESCRIPTION:  Password strength tester



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########

import string

print("Enter your password: ")
password = input()
print()

length = len(password)
upper_count = sum(1 for c in password if c.isupper())
lower_count = sum(1 for c in password if c.islower())
num_count = sum(1 for c in password if c.isdigit())
special_count = sum(1 for c in password if c in string.punctuation)

if length >= 14:
    len_pts = 8
elif length >= 8:
    len_pts = 5
else:
    len_pts = 0

if upper_count >= 3:
    upper_pts = 8
elif upper_count >= 2:
    upper_pts = 4
elif upper_count >= 1:
    upper_pts = 2
else:
    upper_pts = 0

if lower_count >= 3:
    lower_pts = 8
elif lower_count >= 2:
    lower_pts = 4
elif lower_count >= 1:
    lower_pts = 2
else:
    lower_pts = 0

if num_count >= 3:
    num_pts = 8
elif num_count >= 2:
    num_pts = 4
elif num_count >= 1:
    num_pts = 2
else:
    num_pts = 0

if special_count >= 3:
    special_pts = 8
elif special_count >= 2:
    special_pts = 4
elif special_count >= 1:
    special_pts = 2
else:
    special_pts = 0

total_score = (len_pts + upper_pts + lower_pts + num_pts + special_pts) / 40.0
strength_pct = total_score * 100

print("Password Analysis Report")
print("-------------------------")
print(f"LENGTH: {len_pts} points ({length} characters)")
print(f"UPPERCASE: {upper_pts} points ({upper_count} uppercase letter(s))")
print(f"LOWERCASE: {lower_pts} points ({lower_count} lowercase letter(s))")
print(f"NUMBERS: {num_pts} points ({num_count} number(s))")
print(f"SPECIAL CHARACTERS: {special_pts} points ({special_count} special character(s))")
print()
print(f"Total Score: {total_score:.3g}")
print(f"Strength Percentage: {strength_pct:.1f}%")


########### END YER CODE ABOVE THIS LINE ###########










########################################
#          SAMPLE OUTPUT
########################################

'''
Enter your password: password

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 0 points (0 uppercase letter(s))
LOWERCASE: 8 points (8 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.325
Strength Percentage: 32.5%
'''

'''
Enter your password: p@$$WORD

Password Analysis Report
-------------------------
LENGTH: 5 points (8 characters)
UPPERCASE: 8 points (4 uppercase letter(s))
LOWERCASE: 2 points (1 lowercase letter(s))
NUMBERS: 0 points (0 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.575
Strength Percentage: 57.49999999999999%
'''

'''
Enter your password: 123PASwor

Password Analysis Report
-------------------------
LENGTH: 5 points (9 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 0 points (0 special character(s))

Total Score: 0.725
Strength Percentage: 72.5%
'''

'''
Enter your password: 123pasWOR!@#

Password Analysis Report
-------------------------
LENGTH: 5 points (12 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (3 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 0.925
Strength Percentage: 92.5%
'''

'''
Enter your password: 123pasWOR!@#888888888888

Password Analysis Report
-------------------------
LENGTH: 8 points (24 characters)
UPPERCASE: 8 points (3 uppercase letter(s))
LOWERCASE: 8 points (3 lowercase letter(s))
NUMBERS: 8 points (15 number(s))
SPECIAL CHARACTERS: 8 points (3 special character(s))

Total Score: 1.0
Strength Percentage: 100.0%
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. This is one of your first experiences with larger programs - what are three things
   that were challenging for you?


It's size
All the complex code
I have trouble taking the jupiter notebook and applying it to this lab

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
