# FILE NAME - for_loop_start_end_increment.py


# NAME: Luke Kozitsky
# DATE: 10-11-26
# BRIEF DESCRIPTION:  Loop statements with starting and ending increments



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

start = int(input("Starting point: "))
end = int(input("Ending point: "))
step = int(input("Increment by: "))
print(*(range(start, end, step)))


########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Starting point: 3
Ending point: 12
Increment by: 4
3 7 11 
'''


'''
Starting point: 12
Ending point: 22
Increment by: 3
12 15 18 21 
'''


'''
Starting point: 60
Ending point: 10
Increment by: -4
60 56 52 48 44 40 36 32 28 24 20 16 12 
'''
