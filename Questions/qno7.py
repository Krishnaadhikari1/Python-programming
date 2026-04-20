 # Check whether a year is a leap year
year = int(input("Enter the year to check leap year or not: "))

if (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
elif (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")