first, second = 1, 1
for i in range(int(input('Enter length :'))):
    print(first, end=' ')
    first, second = second, first + second


# for i in range(5):
#     print(first, end=' ')
#     first, second = second, first + second
#
# output:
# 1 1 2 3 5
