"""
Magic Number: Sum of the individual digits in a given number until the single digit occurs.
              if the single digit is "1" is called a "Magic Number"
Eg:
    532 # given Number
    5 + 3 + 2 = 10  # repeat until single digit remain
    1 + 0 = 1 --> Magic number

"""

# 1-Approach
num = int(input("Enter a number: "))
temp = num

while temp >= 10:
    s = 0
    while temp:
        rem = temp % 10
        s += rem
        temp //= 10
    temp = s

if temp == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")

# Output:
# Enter a number: 1234
# Magic Number
