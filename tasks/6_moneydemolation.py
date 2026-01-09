"""write a program to display dinominations of currency for given amount
input : 887 Rupees 
output : 
500 x 1 = 500
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01"""

amount = int(input("Enter amount :")) #Getting amount

cr500 = amount//500 #Getting 500 value and upating amount
amount = amount %500 

cr200 = amount//200 #Getting 200 value and upating amount
amount = amount %200

cr100 = amount//100 #Getting 100 value and upating amount
amount = amount %100 

cr50 = amount//50 #Getting 50 value and upating amount
amount = amount %50

cr20 = amount//20 #Getting 20 value and upating amount
amount = amount %20 

cr10 = amount//10 #Getting 10 value and upating amount
amount = amount %10

cr5 = amount//5 #Getting 5 value and upating amount
amount = amount %5

cr2 = amount//2 #Getting 2 value and upating amount
amount = amount %2 #Remaning amount is the value of 1


ans=f"""
500 x 1 = {cr500}
200 x 1 = {cr200}
100 x 1 = {cr100}
50 x 1 = {cr50}
20 x 1 = {cr20}
10 x 1 = {cr10}
5 x 1 =  {cr5}
2 x 1 =  {cr2}
1 x 1 =  {amount}"""

print(ans)



