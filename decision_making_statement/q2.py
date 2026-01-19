# write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 

print("Enter data of farm 1 ")

l1=float(input("Enter length of farm : "))
w1=float(input("Enter width  of farm : "))
a1=l1*w1

print("Enter data of farm 2 ")

l2=float(input("Enter length of farm : "))
w2=float(input("Enter width  of farm : "))
a2=l2*w2

if a1==a2:
    print("Both are equal")

if a1>a2:
    print("1 farm is greater")
if a1<a2:
    print("2 farm is greater ")