# Write a program to calculate total amount after simple interest.


p=int(input("Enter principal amount :"))
r=int(input("Enter rate  :"))
n=int(input("Enter time :"))

amt=(p*r*n)/100
print(f"Amount after interest  is : {amt+p}")