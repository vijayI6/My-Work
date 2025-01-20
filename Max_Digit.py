# find the digit which has maximum frequency in the given Number

num = int(input())
lst = [0] * 10
while num:
    rem = num % 10
    lst[rem] += 1
    num //= 10
print(lst.index(max(lst)), "is the most repeated number")

# Output:
# 222233
#  2
