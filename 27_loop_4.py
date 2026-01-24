'''
Docstring for 27_loop_4
write a program to figure out whether given number is prime number or not 
'''
import sys
no=int(input("Enter number : "))
divisor=2
if(no%2==0 and no!=2):
    print("Number is not prime")
else:
    half=(no//2) + 1
    while divisor<half:
        if no%divisor==0:
            print("Number is not prime")
            sys.exit(1)
        divisor+=1
    print("Number is prime")

