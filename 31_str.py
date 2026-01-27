#for loop with string
# count vowels  

string=input("Enter string : ")
count=0
for letter in string:
    if letter.lower() in ['a','e','i','o','u']:
        count+=1

print(f"Total vowels are :{count}")