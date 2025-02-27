# To print n+nn+nnn... pattern 

num = input() 
size = int(input())  # Number of terms

for i in range(1, size + 1):
    terms = num * i  # Repeat the string 'num' i times
    print(terms, end=' ')  # Print each term

  
# Output:
# number: 3
# number of terms: 4
# 3 33 333 3333 
