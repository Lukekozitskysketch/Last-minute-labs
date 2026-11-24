# FILE NAME - approve_deny.py

# NAME: Luke Kozitsky
# DATE: 11-23-26
# BRIEF DESCRIPTION:  URL Check and logger



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########
import datetime

url = input("Enter a URL to access: ")
print()

with open("approve.txt", "r") as file:
    approve_list = [line.strip() for line in file]

with open("deny.txt", "r") as file:
    deny_list = [line.strip() for line in file]

if url in approve_list:
    status = "APPROVE"
    print("ACCESS GRANTED")
    print("-" * 50)
    print(f"       CONTENT FROM: {url}")
    print("-" * 50)
    print("This website has been verified as safe by your organization.")
    print("Feel free to browse this content for business or educational purposes.")
    print("Remember to follow the organization's acceptable use policy.")
    print("-" * 50)
    print()

elif url in deny_list:
    status = "DENY"
    print("ACCESS DENIED")
    print("-" * 50)
    print(f"       BLOCKED URL: {url}")
    print("-" * 50)
    print("This website has been blocked by your organization's web filter.")
    print("Reason: This URL is on the deny list.")
    print("If you believe this is an error, please contact IT support.")
    print("-" * 50)
    print()

else:
    status = "REVIEW"
    print("URL UNDER REVIEW")
    print("-" * 50)
    print(f"       PENDING REVIEW: {url}")
    print("-" * 50)
    print("This website is not on the approve or deny lists.")
    print("It has been submitted for review by the security team.")
    print("Access is currently restricted until review is complete.")
    print("Please check back later or contact IT if urgent access is needed.")
    print("-" * 50)
    print()
    print("URL has been added to review.txt for security team review.")
    print()

    with open("review.txt", "a") as review_file:
        review_file.write(url + "\n")

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - URL: {url} - STATUS: {status}\n")

print("This access attempt has been logged to log.txt")

########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter a URL to access: www.flcc.edu

ACCESS GRANTED
--------------------------------------------------
       CONTENT FROM: www.flcc.edu
--------------------------------------------------
This website has been verified as safe by your organization.
Feel free to browse this content for business or educational purposes.
Remember to follow the organization's acceptable use policy.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.phishingdemo.org

ACCESS DENIED
--------------------------------------------------
       BLOCKED URL: www.phishingdemo.org
--------------------------------------------------
This website has been blocked by your organization's web filter.
Reason: This URL is on the deny list.
If you believe this is an error, please contact IT support.
--------------------------------------------------

This access attempt has been logged to log.txt
'''

'''
Enter a URL to access: www.opencompsci.com

URL UNDER REVIEW
--------------------------------------------------
       PENDING REVIEW: www.opencompsci.com
--------------------------------------------------
This website is not on the approve or deny lists.
It has been submitted for review by the security team.
Access is currently restricted until review is complete.
Please check back later or contact IT if urgent access is needed.
--------------------------------------------------

URL has been added to review.txt for security team review.

This access attempt has been logged to log.txt
'''

