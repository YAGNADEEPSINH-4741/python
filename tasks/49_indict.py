#write a program to findout whether particular key/value exist in dictionary or not using in operator 

fruits = {
    "apple": 120,
    "banana": 40,
    "mango": 150,
    "grapes": 80
}

check=input("Enter key which is present in dictonary :")
print(check in fruits)

check=input("Enter key which is not present in dictonary :")
print(check not in fruits)