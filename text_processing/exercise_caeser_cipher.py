message = input()
encoded_message = ""
for idx in range(len(message)):
    encoded_message += message[idx:idx+1].replace(message[idx], chr(ord(message[idx])+3))
print(encoded_message)