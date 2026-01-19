"""
     if decision making 
        1) write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM 

        input : 11 hours 
        output  11 AM 

        input : 25 hours 
        output  invalid input 
 """

hour = int(input("Enter hour : "))

if hour<=0 or hour>24:
    print("Invalid input")
if hour>12:
    print(f"{hour-12} PM")
if hour<12:
    print(f"{hour} AM")