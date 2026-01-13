# write a program to findout name of place existing in tuple or not using in operator
#Creating tuple
places = ("delhi", "mumbai", "jaipur", "ahmedabad", "pune", "surat", "chennai", "kolkata", "bangalore", "hyderabad")

find=input("Enter place you like : ")

print("The place u enter is :",find in places,"in list ")

find=input("Enter place you not like : ")

print("The place u enter is :",find not in places ,"in list ")