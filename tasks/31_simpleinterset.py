# Write a program to calculate simple interest using principal, rate, and time.


p=int(input("Enter principal amount :"))
r=int(input("Enter rate  :"))
n=int(input("Enter time :"))

amt=(p*r*n)/100
print(f"Interest is : {amt}")