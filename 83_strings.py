message = " This is cool"
print(len(message))
print(message[5:10])
print(message[5:])
print(message[:5])


print ("Index of first space:",message.index(' '))
first_space_index = message.index(' ')
print ("Text after first space",message [first_space_index:])

last_space_index = message.rindex(' ')
print("Text after last space:", message[last_space_index ])