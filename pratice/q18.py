#Use a loop to count how many times a specific element appears in a list.

lis=[1,2,5,6,1,2,1,1,2,3,4]
search=int(input("Which element u want search :"))
count=0
for no in lis:
    if(no==search):
        count+=1
if count==0:
    print(f"{search} is not in list")
else:
    print(f"{search} is {count} times in list")