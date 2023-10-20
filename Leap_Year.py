# Without Using any module

year = int(input('Enter year:'))
if year % 400 == 0 and year % 100 == 0:
    print('Leap Year')
elif year % 4 == 0 and year % 100 != 0:
    print('Leap Year')
else:
    print('Not a Leap year')

"""
output:
Enter year:2023
Not a Leap year
"""

# Using Calendar module
import calendar

Year = int(input('Enter year:'))
print('Leap Year' if calendar.isleap(Year) else 'Not a Leap Year')  # using Ternary condition

"""
output:
Enter year:2020
Leap Year
"""
