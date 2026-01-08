#write a program to convert given 3 digit amount into words
# input : 175 output : one seven five 



amount = input("Enter Amount :") #GETTING NUMBER

amount =int(amount) #CONVENTING INTO INT
temp =amount


fd = temp//100#GETTING FIRST ELEMENT #156 = 1
temp = temp //10   #15
md = temp %10  #GETTING MIDDLE NUMBER #5
ld = amount % 10 #GETTING LAST ELEMENT #6
print(fd,md,ld)



#LIST OF WORDS
words=['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[fd]+" "+words[md]+" "+words[ld])