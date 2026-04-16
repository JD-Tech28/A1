n=1
m=3
while n<=10:
    #print(n*m)
    n+=1

num=(1,4,9,16,25,36,49,64,91,100)
n=100
idex=0
while idex<len(num):
    if num[idex]==n:
        print("found it at", idex)
    idex+=1

i=1
while i<=5:
    print(i)
    if i==3:
        break
    i+=1

i=1
while i<=10:
    if i==3:
        i+=1
        continue   
    print(i)
    i+=1

i=1
while i<10:
    if(i%2 ==0):
        i+=1
        continue
    print(i)
    i+=1