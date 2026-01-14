#.Create a list and add 3 new elements at the end.

li =[1,5,8,9,11,13,16,41,48]

n1=int(input("Enter 1 element you want to add : "))
n2=int(input("Enter 2 element you want to add : "))
n3=int(input("Enter 3 element you want to add : "))

print(f"Old list was :{li}")

li.append(n1)
li.append(n2)
li.append(n3)

print(f"The new list is : {li}")