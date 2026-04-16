s1=[1,4,9,16,25,36,49,64,91,100,36]
for val in s1:
    print(val)
n=49
idex=0
for val1 in s1: #lineae search
    if s1[idex]==n:
        print("Found the number",n,"at",idex)
    idex+=1