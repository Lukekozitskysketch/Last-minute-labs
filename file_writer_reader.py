# FILE NAME - file_reader_writer.py

# NAME: Luke Kozitsky
# DATE: 11-23-26
# BRIEF DESCRIPTION:  File reader based on user input



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



def main():
    filename = input("File name? ")
    file = open(filename, "a")

    word = input("Word to add? ")
    file.write(word + "\n")

    file.close()

    print()

    file = open(filename, "r")
    print(file.read(), end="")
    file.close()

main()


########################################
#          SAMPLE OUTPUT
########################################

'''
File name? marvel.txt
Word to add? She-Hulk

Steve Rogers
Tony Stark
Thor Odinson
Bruce Banner
Natasha Romanoff
Clint Barton
Sam Wilson
Wanda Maximoff
Pietro Maximoff
The Vision
Scott Lang
Peter Parker
Carol Danvers
Darcy Lewis
Valkyrie
Korg
Miek
Yelena Belova
Hank Pym
She-Hulk
'''


'''
File name? movies.txt
Word to add? Blair Witch Project

Star Wars: Episode I - The Phantom Menace
The Sixth Sense
Toy Story 2
Austin Powers: The Spy Who Shagged Me
The Matrix
Tarzan
Big Daddy
The Mummy
Runaway Bride
Blair Witch Project
'''


'''
File name? pokemon.txt
Word to add? Sandslash

Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
Sandshrew
Sandslash
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Writing to a file isn't terribly hard if you can open a file. But how would you 
   take the contents of a file like the ones in the Sample Output and alphabetize them?
   Make sure you are specific - write down each step.

First open the file in read mode ("r") and use .readlines() to put all the lines into a list then close the file next use .strip() on each word so the hidden \n line breaks dont mess anything up after that use .sort() on the list to put everything in A to Z order then open the same file again in write mode ("w") so it wipes the old unsorted text and finally loop through the sorted list and write each word back with a \n at the end and close it





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
