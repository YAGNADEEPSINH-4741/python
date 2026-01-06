
book = {} #Creating Empty Dictionary

print(book)
#Adding Key value pair
book['name'] = 'Atomic habit'
book['author'] = 'James clear'
book['price'] = 499
print(book)

#adding tuple into dictionary
book['chapters'] = (1,2,3,4,5)
book['topics'] = ['abc','bcd','cde','xyz']
print(book)

#displaying chapter 
print(book['chapters'][0])
print(book['chapters'][1])

#printing 2nd topics
print(book['topics'][2])
book['topics'][2] = 'aabbcc'

print(book)
