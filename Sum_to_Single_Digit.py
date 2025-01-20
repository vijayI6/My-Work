# find the sum of digit until single digit sum can occur

# 1-Approach
num = int(input())
res = ((num - 1) % 9) + 1
print(res)

# 2-Approach
num = int(input())
s = 0
while num:
    s += num % 10
    num //= 10
    if num == 0 and num > 9:
        num = s
        s = 0
print(res)
