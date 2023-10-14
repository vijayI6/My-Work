first, second = 1, 1
for i in range(int(input('Enter length :'))):
    print(first, end=' ')
    first, second = second, first + second
