person = {'name':'rahul sharma','age':40,'weight':74.22,'gender':True,'isMarried':False}
print(person)
print(person['name']) # Output rahul sharma
#updateing Name
person['name'] = "mohal lal"

# adding new key value pair 
person['city'] = 'Delhi'
person['pincode'] = 123456

#deleteing
del person['isMarried']
print(person)