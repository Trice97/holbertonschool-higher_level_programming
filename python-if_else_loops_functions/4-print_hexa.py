#!/usr/bin/python3
# YOUR CODE HERE
output = ""
for i in range(99):
    output += "{} = 0x{:x}\n".format(i, i)
print("{}".format(output), end="")
