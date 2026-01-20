#write a program to findout whether given year is millenium year or not 

year=int(input("Enter year : "))

if len(str(year))!=4:
    print("Invalid year format")
elif year%1000==0:
    print("Millenium year")
else:
    print("Not Millenium year")