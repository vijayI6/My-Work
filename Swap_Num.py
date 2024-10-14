# without using 3 variable
a, b = 3, 4
a, b = b, a
print(a, b)

# using 3 variable
a, b = 3, 4
temp = a
a = b
b = temp
print(a, b)

# using addition and subtraction
a, b = 3, 4
a = a+b  # a = 3+4 --> 7
b = a-b  # b = 7-4 --> 3
a = a-b  # a = 7-3 --> 4
print(a, b)

# using multiplication and division
a, b = 3, 4
a *= b      # a = 3 X 4 --> 12
b = a//b    # b = 12 // 4 --> 3
a = a//b    # a = 12 // 3 --> 4
print(a, b)

# using walrus operator (:=) 
a = 3
b = 4
b = a + b - (a := b)
print(a, b)

# output:
# 4 3
# 4 3
# 4 3
# 4 3
# 4 3
