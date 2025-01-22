# A prime number is a number greater than 1 that is divisible only by 1 and itself, with no other divisors"

def prime(num):
    if num < 2:  # Handle numbers less than 2
        return False
    for ele in range(2, int(num ** 0.5) + 1):
        if num % ele == 0:
            return False
    return True

num1, num2 = map(int, input().split(" "))
for i in range(num1, num2 + 1):
    if prime(i):
        print(i, end=" ")               # It is used to check prime Number in a interval


# num1 = int(input())
# res = prime(num1)
# if res:
#     print(num1)
# else:
#     print('not prime')                  # It is used to check a number is prime or not

# Output:
# 1 100
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

# 3
# 3 is prime
