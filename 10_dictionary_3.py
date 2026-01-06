"""
create dictionary to store 20 different detail about your ownself 
print dictionary
print name, age, gender, dob 
add key value pair pincode into dictionary 
add key value pair to store your 5 favourite touriest destination 
print all the favourite touriest destination 
"""
#creating directory
myself ={
    "name":"Yagnadeepsinh",
    "surname":"Vaghela",
    "dob":14.08,
    "birthyear":2005,
    "age":21,
    "city":"Bhavnagar",
    "state":"GUjarat",
    "country":"India",
    "email":"yagnadeepsinh.4741@gmail.com",
    "education":"Undergraute",
    "College":"Ssccs",
    "Course":"Bca",
    "gender":"Male",
    "programming_languages": ["Python", "C", "JavaScript"],
    "interests": ["Coding", "Technology", "Learning"],
    "hobbies": ["Reading", "Gaming", "Music"],
    "experience_level": "Beginner",
    "projects_completed": 5,
    "github_profile": "https://github.com/YAGNADEEPSINH-4741",
    "learning_focus": "Backend Development"
}

#Printing Dictionary
print(myself)

#printing name, age, gender, dob 
print("Name is :",myself["name"])
print("age is :",myself["age"])
print("gender is :",myself["gender"])
print("Date of birth  is :",myself["dob"])

#Adding new key value pair

myself["pincode"]=364004
print(myself)

#Adding a list of 5 Toursit place

myself["Tourist_place"]=['Bhavnagar', 'Rajkot', 'Surat', 'Ahmedabad', 'Gandhinagar']

#Printing only tourist_place

print("Favourate tourist place are :",myself["Tourist_place"])