#!/usr/bin/python3
# YOUR CODE HERE
alphabet = ""
for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    if char != 'q' and char != 'e':
        alphabet += char
print("{}".format(alphabet), end="")
