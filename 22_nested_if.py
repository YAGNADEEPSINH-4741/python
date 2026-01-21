# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 

price1 = float(input("Enter price of product 1 : "))
weight1=float(input("Enter weight of product 1 :"))

price2 = float(input("Enter price of product 2 : "))
weight2=float(input("Enter weight of product 2 :"))

if price1<=0 or weight1 <=0 or price2<=0 or weight2<=0:
    print("Negative or zero value is not allowed")
else:
    pp1 = price1/weight1
    pp2 = price2/weight2

    if pp1>pp2:
        print("Second product is cheaper : ",pp1-pp2)
    else:
        print("first is cheaper  : ",pp2-pp1)