#Create a list of numbers and use a loop to find and print the average (mean) of all elements in the list.
list=[]
no=int(input("Enter number of elemtent of list :"))
start=1
sum=0
while start<=no:
    list.insert(0,int(input(f"Enter value of {start} element : ")))
    sum+=list[0]
    start+=1

print(f"Average is {sum/no}")
