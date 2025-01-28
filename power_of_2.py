# 1 Approach
num = int(input())
if num <= 0:
    print("No")
if num & num - 1 == 0:
    print("Yes")
else:
    print("No")


# 2-Approach
def powerOfTwo(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return "Yes"
    return "No"

num = int(input())
print(powerOfTwo(num))


# 
# Output:
# 32
# YES
# 6
# No
