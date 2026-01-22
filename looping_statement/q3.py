# 1    -8   27  -64  .....    1000
no=1
sq=0
while sq<1000:
    sq=no*no*no
    if no%2==0:
        sq=0-sq
    print(sq,end=' ')
    no+=1