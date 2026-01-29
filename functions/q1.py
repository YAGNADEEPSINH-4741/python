#write a program to create function that convert given fahrenheit into celsius 
#cel=5/9 (f-32)

def getCelsius(f):
    return 0.5555555555555556 * (f-32)

print(f"Celsius is : {getCelsius(int(input("ENter farenhit : ")))}")