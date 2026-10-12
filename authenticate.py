# FILE NAME - authenticate.py

# NAME: Luke Kozitsky
# DATE: 10-11-26
# BRIEF DESCRIPTION:  Password checker



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

correct_password = "my_secret_password"

while True:
    try:
        user_input = input("Enter password: ")
    except (EOFError, RuntimeError):
        print("Error: This environment does not support terminal inputs.")
        break
    
    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        print("Password does not match.\n")


########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter password: a

Password does not match.
Enter password: b

Password does not match.
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: toomanysecrets

Password does not match.
Enter password: TOOMANYSECRETS

Password does not match.
Enter password: too_Many_Secrets

Password does not match.
Enter password: tooManySecrets

Access granted.
'''

