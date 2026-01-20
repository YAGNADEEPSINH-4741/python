"""
     write a program to accept month number from user and display how many days month has. (use logical operator or)
    input : 1 output : this month has 31 days 
    input : 4 output : this month has 30 days 
"""
mon=int(input("Enter month : "))
mon = int(input("Enter month : "))

if mon == 2:
    print("This month has 29 Days")
elif mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
    print("This month has 31 Days")
elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
    print("This month has 30 Days")
else:
    print("Invalid month number")
