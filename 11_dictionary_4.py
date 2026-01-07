"""Dictionary function 
(Copy, update, print key, values,items,fromkeys,pop,popitem)"""

#Creating Dictionary
person={"name":"abc","age":20,"gender":"male","ismarried":False}
print(person)

#Updating values/if key is not present it automatically creates at end
person["hobbies"]=['travelling','reading']

hobby =['travelling','reading']
#Printing key of dictonary
print(person.keys())

#Printing values of dictonary
print(person.values())

#Printing key values pair of dictonary
print(person.items())

#creatinf new dictory with key from a list 

newdic = dict.fromkeys(hobby)
print(newdic)

#Coping dictonary
# newperson=person mirror copying not good

newperson = person.copy()
print(newperson) 

#poping from dictonary
newperson.pop("name") #Good pratice to do newperson.pop("name",False)
newperson.pop("games",False) #Not causing error because default value is passed
print(newperson)

#poping using item deleting key value from last but return error if list is empty
newperson.popitem()
print(newperson)

#printing both list
print(person,newperson)

