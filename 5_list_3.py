#creating a list 
list=['Yagnadeepsinh',2324324,True,False,'python',None,'chess',47.41]

#Operation in list
print(list)

#update
list[7]=4741
print(list)

#Append
list.append('Ssccs')

#insert
list.insert(0,'Vaghela')
print(list)

#Index

print(list.index('Ssccs'))

#pop
list.pop(2)
print(list)

#remove
list.remove('Ssccs')
print(list)

#delete
del list[5]
print(list)

#copy list
list2 = list.copy()
print(list2)

#clear
list.clear()
print(list,list2)