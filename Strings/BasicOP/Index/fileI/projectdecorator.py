class student():
    def __init__(self,phy,maths):
        self.phy=phy
        self.maths=maths
    @property
    def percentage(self):
       return(((self.phy+self.maths)/2),"%")

S1=student(98,99)
#rint(S1.percentage)
S1.phy=60
#print(S1.percentage)

class number():
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showno(self):
        print(self.real,"i +",self.img,"j")
        return 
    def __add__(self,n2):
        new_real=self.real+n2.real
        newz_img=self.img+n2.img
        return number(new_real,newz_img)
n1=number(3,5)

n2=number(2,3)



class Car():
    def __init__(self,type):
        self.type=type
class toyato(Car):
    def __init__(self,model,type):
        self.model=model
        super().__init__(type)

c1=toyato("VVB","Electric")
print(c1.type)

class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        n=int((22/7)*(self.radius**2))
        print(n,"m^2")
    def perimeter(self):
        m=int(2*self.radius*(22/7))
        print(m,"m")
c1=circle(5)
c1.area()
c1.perimeter()