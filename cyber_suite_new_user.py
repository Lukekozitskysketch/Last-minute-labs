import getpass

name = input("Please enter your name: ")
user_id = input("Please enter your user id: ")
password = getpass.getpass("Please enter your password: ")

print(f"\nWelcome, {name}. Your ID is {user_id}.\n")

masked_password = "X" * len(password)
print(f"PASSWORD: {masked_password}")

