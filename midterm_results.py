# FILE NAME - midterm_results.py

# NAME: Luke Kozitsky
# DATE: 11-8-26
# BRIEF DESCRIPTION:  Math calcutlor and imput reciever 



# WRITE YOUR CODE HERE
def get_choice():
    print("\nPlease choose from the following menu:")
    print("  1. Compute area of a circle")
    print("  2. Compute area of a rectangle\n")
    return input("What is your choice? ")

def main():
    while True:
        print("Welcome to the Mathenator2000")
        results = []
        
        while True:
            choice = get_choice()
            
            if choice == '1':
                radius = float(input("\nWhat is the radius of the circle? "))
                area = 3.141592653589793 * (radius ** 2)
                result_str = f"The area of the circle is {round(area, 2)}"
                print(result_str)
                results.append(result_str)
                
            elif choice == '2':
                length = float(input("\nWhat is the length of the rectangle? "))
                width = float(input("What is the width of the rectangle? "))
                area = length * width
                result_str = f"The area of a rectangle is {area}"
                print(result_str)
                results.append(result_str.replace("a rectangle", "the rectangle"))
                
            else:
                print("\nInvalid selection.")
                
            play_again = input("\nWould you like to play again (y/n)? ").strip().lower()
            if play_again == 'n':
                break
                
        print("\n-------------------------")
        print("A record of your results: ")
        print(results)
        print("\nThank you for using the Mathenator2000\n")
        
        break

if __name__ == "__main__":
    main()
# MEET REQUIREMENTS AS STATED IN BRIGHTSPACE
