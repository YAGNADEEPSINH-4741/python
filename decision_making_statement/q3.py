""" write a program to accept day of week (between 1 to 7) and then display name of day. (use simple if decision making)
            input 1 : monday 
            input 2 : tuesday 
            input 7 : sunday 
"""

no =int(input("Enter number of day : "))
if no<1 or no>7:
    print("invalid input")
if no==1:
    print("monday")
if no==2:
    print("tuesday")
if no==3:
    print("wednesday")
if no==4:
    print("thurday")
if no==5:
    print("friday")
if no==6:
    print("saturday")
if no==7:
    print("sunday")