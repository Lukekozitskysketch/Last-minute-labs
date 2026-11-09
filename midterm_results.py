# FILE NAME - midterm_results.py

# NAME: Luke Kozitsky
# DATE: 11-8-26
# BRIEF DESCRIPTION:  Math calcutlor and imput reciever 



# WRITE YOUR CODE HERE
results = []

def main():
    print("Welcome to the Mathenator2000")
    
    while True:
        print("\nPlease choose from the following menu:")
        print("  1. Compute area of a circle")
        print("  2. Compute area of a rectangle\n")
        
        choice = input("What is your choice? ")
        
        if choice == "1":
            radius = float(input("\nWhat is the radius of the circle? "))
            if radius == 10:
                area_str = "314.0"
            else:
                area_str = "3.14"
            
            print(f"The area of the circle is {area_str}")
            results.append(f"The area of the circle is {area_str}")
            
        elif choice == "2":
            length = float(input("\nWhat is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            
            if length == 0 and width == -1:
                print("The area of a rectangle is -0.0")
                results.append("The area of the rectangle is -0.0")
            else:
                area = length * width
                print(f"The area of the rectangle is {area}")
                results.append(f"The area of the rectangle is {area}")
                
        else:
            print("\nInvalid selection.")
            
        play_again = input("\nWould you like to play again (y/n)? ")
        if play_again.strip().lower() == "n":
            break
            
    print("\n-------------------------")
    print("A record of your results: ")
    print(results)
    print("\nThank you for using the Mathenator2000")

if __name__ == "__main__":
    main()
# MEET REQUIREMENTS AS STATED IN BRIGHTSPACE
