"""
    write a program to accept 2 number from user. and accept choice for operations.
    operations will be addition, subtraction, multiplication, division
    do operation and display result as per user choice using switch statements.
"""

n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 :"))
ch=int(input("""
                1.for addition
                2.for subtraction
                3.for mutiplication
                4.for division
                Enter your choice :"""))

if ch==1:
    print(f"Addition is : {n1+n2}")
elif ch==2:
    print(f"Subtraction is : {n1-n2}")
elif ch==3:
    print(f"Multiplication is : {n1*n2}")
elif ch==4:
    print(f"Divison is : {n1/n2}")
else:
    print("Invalid choice ")
