# Using Logic
first, second = 1, 1
sizes = int(input())
for i in range(sizes):
    print(first, end=' ')
    first, second = second, first + second


# Using Recursion
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


size = int(input("Enter"))
for i in range(size):
    print(fibonacci(i), end=" ")

# output:
# 5
# 1 1 2 3 5
# 1 1 2 3 5
