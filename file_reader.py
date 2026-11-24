# FILE NAME - file_reader.py

# NAME: Luke Kozitsky 
# DATE: 11-23-26
# BRIEF DESCRIPTION:  File reader



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




filename = input("File name? ")
print()

with open(filename, "r") as file:
    print(file.read(), end="")

########################################
#          SAMPLE OUTPUT
########################################

'''
File name? words01.txt

Wolverine
Rogue
Psylocke
Professor X
Beast
'''


'''
File name? words02.txt

Lily
Marshall
Barney
Robin
Ted
'''


'''
File name? words03.txt

blubber
macadamia
gazebo
spatula
plethora
ploy
foible
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is an example of a time when you might want to output the contents
   of a file?

Display a text file





'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[X] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[X] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
