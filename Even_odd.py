# using modulo operator
num = int(input())
if num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

# without using modulo operator
num = int(input())
if num & 1 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

# using bin() function or without using & operator
num = int(input())
if bin(num)[-1] == '0':
    print(f'{num} is even')
else:
    print(f'{num} is odd')

# without using if block
num = int(input())
lst = ['even', "odd"]
print(f'{num} is {lst[num % 2]}')


# output:
# 10 is even
# 30
# 30 is even
# 45
# 45 is odd
# 67
# 67 is odd
