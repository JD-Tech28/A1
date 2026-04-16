import random

num=random.randint(1,100)
total=0
while True:
    y=int(input("Guess the number:"))
    total+=1
    if num==y:
        print ("correct")
        break
    else:
        print("Incorrect")
    if num>y:
        print("up")
    else:
        print("down")

print("No. of trails:",total)

