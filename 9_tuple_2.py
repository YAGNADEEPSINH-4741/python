"""
    create tuple to store all states name of india 
    display tuple 
    display 1st five items 
    display 2nd and 3rd and 4th item 
    display all items from 7th position onwards 
    try to remove 3rd item see what happens 
"""
# Creating tuple
states= ("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")
# Displaying tuple
print(states)

# Displaying 1st 5 item
print("Displaying 5 item :",states[:5])

#Displaying 2 to 4 item
print("Displaying 2 to 4 item : ",states[2:5])

#Displaying all item from 7 position
print("Displaying from 7 item : ",states[7:])

#Deleting 3 item  it will cause error since tuple is inmutable
#del states[3]
#print(states)