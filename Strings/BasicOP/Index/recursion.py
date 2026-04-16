def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

def F(n):
    if n==1:
        return 1
    return F(n-1)*n

print(F(5))

def sum(a):
    if(a==0):
        return 0
    return sum(a-1)+a

print(sum(2))


def x(Q,idex=0):
    if(idex==len(Q)):
        return 
    print(Q[idex])
    x(Q,idex+1)

r=("jd","sd","vd")

x(r)

with open("D:\jeevan D\SMS Project\Strings\BasicOP\Index\pratice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")

with open("D:\jeevan D\SMS Project\Strings\BasicOP\Index\pratice.txt","w") as f:
    f.write(new_data)