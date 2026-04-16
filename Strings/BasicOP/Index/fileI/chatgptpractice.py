x=51
count=2

while True:
    i=int(input("Enter number:"))
    if(i==x):
        print("Correct")
        break
    else:
        print("incorrect")
        count+=1
    if(i>x):
        print("Down")
    else:
        print("up")

print("No. of trial:",count)

