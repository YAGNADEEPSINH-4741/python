#Create a tuple of numbers and find the largest element

tp =(10,15,20,18,30,36,14,95)
tp=list(tp)
tp.sort()
tp.reverse()
print(f"The max element in tuple is : {tp[0]}")
tp=tuple(tp)