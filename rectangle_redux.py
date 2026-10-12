# FILE NAME - rectangle_redux.py

# NAME: Luke Kozitsky
# DATE: 10-11-26
# BRIEF DESCRIPTION:  Rectangle size creater



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
import sys

try:
    user_input = input("How tall would you like the rectangle? \n")
    if not user_input.strip():
        sys.exit(0)
    hollow_rows = int(user_input)
except (EOFError, ValueError, RuntimeError):
    sys.exit(0)

print("*****")
for _ in range(hollow_rows):
    print("*   *")
print("*****")


########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
How tall would you like the rectangle? 3
*****
*   *
*   *
*   *
*****
'''


'''
How tall would you like the rectangle? 1
*****
*   *
*****
'''


'''
How tall would you like the rectangle? 0
*****
*****
'''


'''
How tall would you like the rectangle? 10
*****
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*****
'''

