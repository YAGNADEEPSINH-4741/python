set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1,set2)
# unique values
set3 = set1.union(set2)
print(set3)
#common values
set4 = set1.intersection(set2)
print(set4)

#values not there in set 2 
set5 = set1.difference(set2)
print(set5)

#Duplicate value list
numbers = [12, 18, 25, 31, 37, 42, 48, 53, 57, 61, 70, 74, 78, 82, 86, 92, 96, 99,12,18,48]
print(numbers)
print(len(numbers)) #length of list
#Converting list into set
unique_numbers = set(numbers) 
print(unique_numbers)