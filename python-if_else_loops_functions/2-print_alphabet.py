#!/usr/bin/python3
# YOUR CODE HERE
alphabet = ""
for i in range(ord('a'), ord('z') + 1):
    alphabet += chr(i)
print("{}".format(alphabet), end="")
