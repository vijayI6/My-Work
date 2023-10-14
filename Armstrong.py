"""
Question 2:
Armstrong Number or Not
"""
# Approach 1 (Class) approach
x = int(input("Enter a number:"))
temp = copy = x
s = 0
length = len(str(x))
while copy > 0:
    r = copy % 10
    s = s + pow(r, length)
    copy = copy // 10
if s == x:
    print("{} is Armstrong number".format(x))
else:
    print("{} is not a Armstrong number".format(x))

# Approach 2 (Own) apporach

s = input('Enter a number:')
le = len(s)
# lst = [i ** le for i in list(map(int, s))]
lst = [pow(i, le) for i in list(map(int, s))]

if int(s) == sum(lst):
    print(f"{s} is Armstrong number")
else:
    print(f"{s} is not a Armstrong number")
