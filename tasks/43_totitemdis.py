#Write a program to calculate discount amount using price and discount rate.


i1=int(input("Enter price of item 1 :"))
i2=int(input("Enter price of item 2 :"))
i3=int(input("Enter price of item 3 :"))
i4=int(input("Enter price of item 4 :"))
i5=int(input("Enter price of item 5 :"))

dis=float(input("Enter discount percentage :"))


amt=i1+i2+i3+i4+i5
disamt=amt*dis/100

print(f"THE AMOUNT IS :{amt-disamt}")