# To print n+nn+nnn... pattern 

num = input("Enter a number: ")  # Input as a string for concatenation
size = int(input("Enter the number of terms: "))  # Number of terms

for i in range(1, size + 1):
    terms = num * i  # Repeat the string 'num' i times
    print(terms, end=' ')  # Print each term

  
# Output:
# Enter a number: 3
# Enter the number of terms: 4
# 3 33 333 3333 
