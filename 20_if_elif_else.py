#write a program to find out profit or loss amount from user given purchase and sell price of project
#input purchase & sell price

price=int(input("Enter purchase price : "))
sell=int(input("Enter sales price : "))
diff=sell - price

if diff>0:
    print(f"Profit of {diff} Rs")
elif diff<0:
    print(f"Loss of {diff} Rs")
else:
    print("No profit no loss")