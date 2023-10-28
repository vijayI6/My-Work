"""
To print Floyd's Triangle using for loop
*
* *
* * *
* * * *
* * * * *

"""
# using for loop
n = int(input("Enter size of the Triangle:"))
for i in range(n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Using while loop to print the triangle
s = int(input("Enter size:"))
a = 1
while a <= s:
    print("* " * a)
    a += 1
