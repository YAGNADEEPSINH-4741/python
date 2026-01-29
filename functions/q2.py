#write a program to create function that calculate and return simple interest of given amount rate and year 


def getSimpleInterest(p,r,n):
    return (p*r*n)/100

p=int(input("Enter Prinicipal Amount :")) 
r=float(input("Enter rate of interest :"))
n=int(input("Eneter NUmber of year :"))
print(f"Simple Interest is :{getSimpleInterest(p,r,n)}")