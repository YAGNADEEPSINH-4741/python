#Create a list and delete one specific element from it.

l1=[1,8,9,10,15,25,31,49]

ch=int(input("Enter element you want to delete : "))
print(f"The old list is : {l1}")
l1.remove(ch)

print(f"The new list is : {l1}")