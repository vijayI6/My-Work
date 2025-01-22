# find the digit that has the maximum frequency in the given Number

num = int(input())
lst = [0] * 10
while num:
    rem = num % 10
    lst[rem] += 1
    num //= 10
print(lst.index(max(lst)), "is the most repeated number")


# By Using List
num = int(input())
lst = list(str(num))
res = max(lst, key=lst.count)
print(f"Most repeated element: {res}")


# Output:
# 222233
# 2
