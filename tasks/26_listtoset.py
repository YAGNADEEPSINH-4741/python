#Given two lists, convert them into sets and find common elements.

l1=[1,2,3,4,5,6,7,8,9,10]
l2=[2,3,5,6,11,12,1,2]

l1=set(l1)
l2=set(l2)

print(f"Common elements are {l1.intersection(l2)}")

