"""
     write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18

    Pisces: February 19–March 20
"""


mz=""
d=int(input("Enter day of birth"))
m=int(input("Enter birth month:"))

if (m == 1 and d > 31) or (m == 2 and d > 28) or (m == 3 and d > 31) or (m == 4 and d > 30) or \
   (m == 5 and d > 31) or (m == 6 and d > 30) or (m == 7 and d > 31) or (m == 8 and d > 31) or \
   (m == 9 and d > 30) or (m == 10 and d > 31) or (m == 11 and d > 30) or (m == 12 and d > 31) or\
   (m<0 or m>12) or d<1 :
    print("Invalid information entered")
else:
    if(d>=21 and m==3) or (d<=19 and m==4):
        mz="Aries"
    elif(d>=20 and m==4) or (d<=20 and m==5):
        mz="Taurus"
    elif(d>=21 and m==5) or (d<=20 and m==6):
        mz="Gemini"
    elif(d>=21 and m==6) or (d<=22 and m==7):
        mz="Cancer"
    elif(d>=23 and m==7) or (d<=22 and m==8):
        mz="Leo"
    elif(d>=23 and m==8) or (d<=22 and m==9):
        mz="Virgo"
    elif(d>=23 and m==9) or (d<=22 and m==10):
        mz="Libra"
    elif(d>=23 and m==10) or (d<=21 and m==11):
        mz="Scorpio"
    elif(d>=22 and m==11) or (d<=21 and m==12):
        mz="Sagittarius"
    elif(d>=22 and m==12) or (d<=19 and m==1):
        mz="Capricorn"
    elif(d>=20 and m==1) or (d<=18 and m==2):
        mz="Aquaius"
    elif(d>=19 and m==2) or (d<=20 and m==3):
        mz="Pisces"
    else:
        print("Invalid while assigniment of sign")

print(f"Zeodic Sign is {mz}")
