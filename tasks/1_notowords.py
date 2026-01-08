"""
 THIS PROGRAM CREATE A 2 DIGIT NUMBER INTO WORDS
 EXAMPLE INPUT 65 OUTPUT SIX FIVE
 IT WORKS IN 2 DIGIT VALUES ONLY
"""
amount = input("Enter Amount :") #GETTING NUMBER

amount =int(amount) #CONVENTING INTO INT



fd = amount//10 #GETTING FIRST ELEMENT
ld =amount%10 #GETTING LAST ELEMENT


#LIST OF WORDS
words=['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[fd]+" "+words[ld])