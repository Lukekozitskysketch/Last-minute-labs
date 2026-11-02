# FILE NAME - fortune_machine.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



    ########## ENTER YER CODE BELOW THIS LINE ##########
import fortune_util

def main():
    while True:
        try:
            fortune_util.get_directions()
            fortune_util.dashes()
            
            choice = input().strip().upper()
            
            if choice == '1':
                print("ONE FORTUNE:")
                fortune_util.get_one_fortune()
                fortune_util.dashes()
                fortune_util.quit()
            elif choice == 'M':
                print("MULTIPLE FORTUNES:")
                num_str = input("How many fortunes would you like? ")
                num = int(num_str)
                fortune_util.get_multiple_fortunes(num)
                fortune_util.dashes()
                fortune_util.quit()
            elif choice == 'Q':
                break
            else:
                print("Invalid choice. Please try again.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
    ########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################

'''

--------------------------------------------------
Welcome to the Fortune Telling Machine

The instructions are simple - you may request one
fortune, you  may request multiple fortunes, or you
may request to quit.

Please enjoy your fortune(s)! But beware! When you use
the Fortune Telling Machine, you get what you get and
you don't get upset!

--------------------------------------------------
ONE FORTUNE:
There's a lot of atoms in you.


--------------------------------------------------
MULTIPLE FORTUNES:
How many fortunes would you like? 7

1 - Bring an umbrella today.

2 - There's a lot of atoms in you.

3 - You will live a long, prosperous life.

4 - Chin up! It's going to be a great day!

5 - If you have no pockets, your phone can't fall out of them!

6 - Chin up! It's going to be a great day!

7 - You will live a long, prosperous life.

--------------------------------------------------

I hope you enjoyed your fortunes...

'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 






2. What value do you see in having external modules?






'''


