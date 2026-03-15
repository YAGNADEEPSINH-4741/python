# String creation
text = "Python Programming"

print("String:", text)

# Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# Slicing
print("First 6 characters:", text[:6])
print("Last 6 characters:", text[-6:])
print("Reversed string:", text[::-1])

# String methods
print("Upper case:", text.upper())
print("Lower case:", text.lower())
print("Replace word:", text.replace("Python", "Java"))

# Character checking
s = "Python123"
print("Is Alphanumeric:", s.isalnum())
print("Count of 'o':", text.count("o"))