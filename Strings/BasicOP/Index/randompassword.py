import random
import string

password=""
n=6  # length of the password
for i in range(n):
    pin=random.choice(string.ascii_letters+ string.punctuation + string.digits)
    password+=pin


pin2=(string.ascii_letters+ string.punctuation + string.digits)
password2="".join([random.choice(pin2)for i in range(n)])


guess=random.randint(1,100)
count=0
while True:
    num=int(input("guess the number:"))
    if num==guess:
        print("correct")
        break
    else:
        print("Incorrect")
    count+=1
    if num>guess:
        print("down")
    else:
        print("up")
    
print("no. of trails",count)