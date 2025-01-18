"""
GCD : Greatest common divisor --> factors of the given numbers
                             ---> max common factor of the given numbers ---> GCD
Ex:
    12, 14 # given numbers
    12 --> 1, 2, 3, 4, 6, 12
    14 --> 1, 2, 14, 7

    1,2 are common factors --> '2' is gcd of 12 and 14

"""

# Gcd of Two Numbers Using Math Module
import math

num = int(input())
num1 = int(input())
print(f'The Gcd of {num} and {num1} is {math.gcd(num, num1)}')


# Gcd of Two Numbers Without Using Math Module
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num = int(input())
num1 = int(input())

gcd = find_gcd(num, num1)
print(f"The GCD of {num} and {num1} is {gcd}")

# Output:
# 12
# 23
# The Gcd of 12 and 23 is 1
