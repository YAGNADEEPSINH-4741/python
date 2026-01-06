#Creating tuple

nations = ("India", "United States", "China", "Russia", "Germany", "France", "Japan", "Brazil", "United Kingdom", "Australia","India","Sri lanka","India")
box= (100,True,1.25,'Bhavnagar',None)

#Printing all items
print(nations)
#Display oth nation
print(nations[0])

#display 0 to 3 element
print(nations[1:4])

#display all the items from 5th position onwards
print(nations[5:])

#Displaying index of Russia
print(nations.index("Russia"))

#Counting how many times India is present
print(nations.count("India"))


#Displaying Tuple 2 time
print(nations*2)

#Concentrate 2 tuple
print(nations+box)
