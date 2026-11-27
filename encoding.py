import base64

filename = input("File name? ")

with open(filename, "rb") as file:
    raw_data = file.read()

encoded_data = base64.b64encode(raw_data)

print(encoded_data)
