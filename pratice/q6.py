#Create a tuple of numbers and find the smallest element

tp =(15,10,1,20,18,30,36,14,95)
tp=list(tp)
tp.sort()
tp=tuple(tp)
print(f"The min element in tuple is : {tp[0]}")
