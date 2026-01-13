#write a program to findout whether number exist in list or not using in operator


numbers = [12, 45, 7, 89, 23, 56, 91, 34, 68, 10]

chk =int(input("Enter number in list  :"))
print("Number is in ",chk in numbers)

chk =int(input("Enter number in not  list  :"))
print("Number is in ",chk not in numbers)