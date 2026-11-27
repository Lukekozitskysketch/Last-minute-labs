# Luke Kozitsky
#11-27-26
# hashing based on user input
import hashlib

message = input("Enter the message to hash: ")
hashed = hashlib.sha256(message.encode()).hexdigest()
print("Hashed: ", hashed)


'''
SAMPLE OUTPUT

Enter the message to hash: This is the clock song
Hashed:  edc91007e1124dd314738386e145f6af73e959804d9d493f8d584aa8fe093273

Enter the message to hash: a
Hashed:  ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
'''
