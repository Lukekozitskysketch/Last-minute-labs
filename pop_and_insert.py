# FILE NAME - pop_and_insert.py

# NAME: Luke Kozitsky
# DATE: 10-26-26
# BRIEF DESCRIPTION:  cut and re insert code



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




# Declare an array called `customers`.


# Declare a variable called `driver_name` and set it equal to ''.


# Collect information from the user. The user can keep entering 
# names of drivers as they enter the DMV. Once the last driver
# is loaded into the list, the DMV employee will type 'EOF' 
# (which in computer nerdom translates to "End of File").


    # Need to ensure that "EOF" is not input into the system as a name!




# Output the names




#########################################
#               YOUR JOB:               #
#                                       #
# 1. Move the first item in the list to #
#    be the last item                   #
#                                       #
#########################################

########## ENTER YER CODE BELOW THIS LINE ##########


def manage_customer_list():
    customers = []
    
    while True:
        name = input("Enter the name of the customer: ")
        if name == "EOF":
            break
        customers.append(name)
    
    print()
    print(customers)
    
    if customers:
        shifted_customers = customers[1:] + [customers[0]]
        print(shifted_customers)
    else:
        print([])

manage_customer_list()







########### END YER CODE ABOVE THIS LINE ###########
    




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the name of the customer: Alice
Enter the name of the customer: Bob
Enter the name of the customer: Charlie
Enter the name of the customer: Danielle
Enter the name of the customer: EOF

['Alice', 'Bob', 'Charlie', 'Danielle']
['Bob', 'Charlie', 'Danielle', 'Alice']
'''


'''
Enter the name of the customer: Eliza
Enter the name of the customer: EOF

['Eliza']
['Eliza']
'''


'''
Enter the name of the customer: 1234
Enter the name of the customer: 2345
Enter the name of the customer: 3456
Enter the name of the customer: 4567
Enter the name of the customer: EOF

['1234', '2345', '3456', '4567']
['2345', '3456', '4567', '1234']
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. How did you move the element in the list?

slicing everything from the second item onward and making a new list containing just the first item at the  end.





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
[X] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
