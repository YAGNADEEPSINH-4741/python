#Create a dictionary and calculate the average of all values.


stud={
    "rohit":80,"mohit":60,"varu":70,"om":99,"raj":45
}
marks=list(stud.values())

print(f"Average is : {sum(marks)/len(marks)}")