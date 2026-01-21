# write a program to find out whether given year is leap year or not
# https://www.wikihow.com/Calculate-Leap-Years

year=int(input("Enter year : "))

if year<1:
    print("Invalid year ")
else:
    rem1 =year %4
    rem2 =year %100
    rem3=year %400
    if (rem1==0 and rem2!=0) or (rem2==0 and rem3==0):
        print("Given is leap year")
    else:
        print("Not a leap year")