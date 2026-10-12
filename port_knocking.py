# FILE NAME - port_knocking.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########









########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
===== PORT KNOCKING FIREWALL SIMULATOR =====
This firewall requires a specific sequence of port connections.
You have 3 attempts to find the correct sequence.
(Hint: Enter ports as integers, one at a time)

Attempt 1 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 3
Enter port number: 4
Enter port number: 5
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 3 knocks, but the firewall expects 4.

Attempt 2 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 2222
Enter port number: 3333
Enter port number: 4444
Enter port number: 5555
Enter port number: 0

FIREWALL RESPONSE: Connection accepted!
Correct port knocking sequence detected.
Firewall has opened port 22 for your connection.
'''

'''
===== PORT KNOCKING FIREWALL SIMULATOR =====
This firewall requires a specific sequence of port connections.
You have 3 attempts to find the correct sequence.
(Hint: Enter ports as integers, one at a time)

Attempt 1 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 2222
Enter port number: 3333
Enter port number: 4444
Enter port number: 5555
Enter port number: 0

FIREWALL RESPONSE: Connection accepted!
Correct port knocking sequence detected.
Firewall has opened port 22 for your connection.
'''

'''
===== PORT KNOCKING FIREWALL SIMULATOR =====
This firewall requires a specific sequence of port connections.
You have 3 attempts to find the correct sequence.
(Hint: Enter ports as integers, one at a time)

Attempt 1 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 1
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 1 knocks, but the firewall expects 4.

Attempt 2 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 2
Enter port number: 3
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 2 knocks, but the firewall expects 4.

Attempt 3 of 3:
Enter your port knock sequence. Enter 0 when finished.
Enter port number: 4
Enter port number: 5
Enter port number: 6
Enter port number: 0

FIREWALL RESPONSE: Connection rejected!
Your sequence had 3 knocks, but the firewall expects 4.

MAXIMUM ATTEMPTS REACHED
Firewall has blocked your IP address for 30 minutes.
The correct sequence was: [2222, 3333, 4444, 5555]
'''
