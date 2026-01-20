"""
Write a program that takes a 5 subject marks from user. calculate total and average  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| below 50   | Need to improve  |
----------------------------------------
"""

marks=[]
marks.append(int(input("Enter marks of subject 1 :")))
marks.append(int(input("Enter marks of subject 2 :")))
marks.append(int(input("Enter marks of subject 3 :")))
marks.append(int(input("Enter marks of subject 4 :")))
marks.append(int(input("Enter marks of subject 5 :")))

tot=sum(marks)
avg=tot/5

if avg>=90:
    print(f"Percentage is {avg} Grade is A+")
elif avg>=80:
    print(f"Percentage is {avg} Grade is A")
elif avg>=70:
    print(f"Percentage is {avg} Grade is B")
elif avg>=60:
    print(f"Percentage is {avg} Grade is C")
elif avg>=50:
    print(f"Percentage is {avg} Grade is D")
else:
    print(f"Need to improve percentage is :{avg}")

