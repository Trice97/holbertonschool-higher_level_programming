#!/usr/bin/python3
# YOUR CODE HERE
output = ""
for i in range(10):
    for j in range(i + 1, 10):
        output += "{:02d}".format(i * 10 + j)
        if i < 8:
            output += ", "
print("{}".format(output))
