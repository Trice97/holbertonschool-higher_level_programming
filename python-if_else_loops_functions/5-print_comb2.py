#!/usr/bin/python3
# YOUR CODE HERE
output = ""
for i in range(100):
    output += "{:02d}".format(i)
    if i < 99:
        output += ", "
print("{}".format(output))
