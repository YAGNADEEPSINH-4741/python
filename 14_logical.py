num1 =100 
num2 =200
num3 =300
res=num1 < num2 and num2 < num3
print(f"{res} = {num1} > {num2} and {num2} > {num3}")

res=num1 > num2 or num2 < num3
print(f"{res} = {num1} > {num2} or {num2} < {num3}")

res=not (num1 > num2 and num2 > num3)
print(f"{res} = not {num1} > {num2} and {num2} > {num3}")