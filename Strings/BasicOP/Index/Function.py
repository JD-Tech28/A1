def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum

calc_sum(10,12)

def calc_avg(a,b,c):
    Avg=(a+b+c)/3
    print(Avg)
    return Avg

calc_avg(10,20,30)

def mul(a,b):
    Mul=a*b
    print(Mul)
    return Mul

mul(2,2)

def Fact(a):
    act=1
    for i in range(1,a+1):
        act*=i
    print(act)

Fact(5)
Fact(3)

def rupee(a):
    dollars=a*92
    print("price:",dollars,end="$")

rupee(10)
