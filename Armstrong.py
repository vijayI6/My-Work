"""
Question 2:   given number is Narcissistic / Armstrong Number  or Not?

"""

# Approach 1 (Class) approach
num = int(input("Enter a number:"))
temp = num
res = 0
length = len(str(num))
while temp:
    rem = temp % 10
    res += pow(rem, length)
    temp//=  10
if res == num:
    print("{} is Armstrong number".format(num))
else:
    print("{} is not a Armstrong number".format(num))




# Approach 2 (Own) apporach
s = input('Enter a number:')
le = len(s)
# lst = [i ** le for i in list(map(int, s))]
lst = [pow(i, le) for i in list(map(int, s))]

if int(s) == sum(lst):
    print(f"{s} is Armstrong number")
else:
    print(f"{s} is not a Armstrong number")
