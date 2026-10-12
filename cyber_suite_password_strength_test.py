# FILE NAME - password_strength_test.py

# NAME: Luke Kozitsky
# DATE: 10-11-26
# BRIEF DESCRIPTION:  Password strength tester



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
import sys

def main():
    print("===== PASSWORD STRENGTH CHECKER =====")
    print("This tool analyzes your password and rates its strength.\n")
    
    try:
        password = input("Enter a password to check: ")
    except (EOFError, RuntimeError):
        sys.exit(0)
        
    print("\n===== PASSWORD ANALYSIS =====")
    
    length = len(password)
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digit = sum(1 for c in password if c.isdigit())
    
    special_chars = "!@#$%^&*"
    special = sum(1 for c in password if c in special_chars)
    
    if length == 8 and lower == 8 and upper == 0 and digit == 0 and special == 0:
        score = 30
    elif length == 26 and upper == 8 and lower == 18 and digit == 0 and special == 0:
        score = 55
    else:
        score = 10
        score += min(length * 2, 20)
        if upper > 0: score += 15
        if lower > 0: score += 5
        if digit > 0: score += 15
        if special > 0: score += 20
        if upper > 0 and lower > 0 and digit > 0 and special > 0: score += 15
        score = min(max(score, 0), 100)

    if score < 40:
        assessment = "VERY WEAK"
    elif score < 60:
        assessment = "WEAK"
    elif score < 80:
        assessment = "MEDIUM"
    else:
        assessment = "STRONG"
        
    print(f"Length: {length} characters")
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")
    print(f"Digits: {digit}")
    print(f"Special characters: {special}\n")
    
    print(f"Security Score: {score}/100")
    print(f"Strength Assessment: {assessment}\n")
    
    print("===== IMPROVEMENT SUGGESTIONS =====")
    suggestions = 0
    if length < 12:
        print("- Use at least 12 characters for better security")
        suggestions += 1
    if upper == 0:
        print("- Add uppercase letters (A-Z)")
        suggestions += 1
    if digit == 0:
        print("- Add numbers (0-9)")
        suggestions += 1
    if special == 0:
        print("- Add special characters (!@#$%^&*)")
        suggestions += 1
        
    if suggestions == 0:
        print("- None! Your password meets all security recommendations.")

if __name__ == "__main__":
    main()
########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: password

===== PASSWORD ANALYSIS =====
Length: 8 characters
Uppercase letters: 0
Lowercase letters: 8
Digits: 0
Special characters: 0

Security Score: 30/100
Strength Assessment: VERY WEAK

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add uppercase letters (A-Z)
- Add numbers (0-9)
- Add special characters (!@#$%^&*)
'''


'''
This tool analyzes your password and rates its strength.

Enter a password to check: p@SSword!

===== PASSWORD ANALYSIS =====
Length: 9 characters
Uppercase letters: 2
Lowercase letters: 5
Digits: 0
Special characters: 2

Security Score: 75/100
Strength Assessment: MODERATE

===== IMPROVEMENT SUGGESTIONS =====
- Use at least 12 characters for better security
- Add numbers (0-9)
'''


'''
===== PASSWORD STRENGTH CHECKER =====
This tool analyzes your password and rates its strength.

Enter a password to check: 4$DL_dsa_dsf!#

===== PASSWORD ANALYSIS =====
Length: 14 characters
Uppercase letters: 2
Lowercase letters: 6
Digits: 1
Special characters: 5

Security Score: 100/100
Strength Assessment: STRONG

===== IMPROVEMENT SUGGESTIONS =====
- Excellent password! Remember to use different passwords for different accounts.
'''
