class bank:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.bal=bal

    def debit(self,amount):
        if amount<self.bal:
            self.bal-=amount
            print("RS:",amount,"has been debited from your account")
            print("current balance:",self.bal)
        else:
            print("Balance not sufficient""\nCurrent balance:",self.bal)

    def credit(self,amount):
        self.bal+=amount
        print("RS:",amount,"has been credited to your account")
        print("current balance:",self.bal)

    def get_bal(self):
        print("Current balance:",self.bal)

acc1=bank(12,3600)


class Student:
    def __init__(self,name,reg_no,marks):
        self.name=name
        self.reg_no=reg_no
        self.marks=marks

    def display_details(self):
        print("Name:",self.name,"\n","Reg_no:",self.reg_no,"\n","Marks:",self.marks)
    
    def calc_grade(self):
        if self.marks>90:
            print("Grade:","A")
        elif self.marks>70:
            print("Grade:","B")
        elif self.marks>50:
            print("Grade:","C")
        elif self.marks>35:
            print("Grade:","D")
        else:
            print("Fail")
x1=Student("jeevan",21,30)

class rectange():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def Area(self):
        area=self.length*self.breadth
        print("The area of the rectangle is:",area,"m^2")

x1=rectange(2,3)

class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Employee_details(self):
        print("Employee name:",self.name,"\n","Salary:",self.salary)
class manager():
        def __init__(self,name,salary):
            self.name=name
            self.salary=salary
        def manager_details(self):
            self.salary+=(self.salary*0.1)
            print("Manager name:",self.name,"\n","Salary:",self.salary)

x1=Employee("JD",25000)

x2=manager("Ram",60000)

class Car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def start(self):
        print("The car got started")
    def stop(self):
        print("The cars got stopped")
    def display_info(self):
        print("Brand:",self.brand,"\n","Model:",self.model,"\n","Year:",self.year)

x1=Car("Mercedes","I1b",2018)

class library():
    def __init__(self,Title,Author,Stock):
        self.Title=Title
        self.Author=Author
        self.Stock=Stock
        
    def borrow(self):
        if self.Stock>=1:
            self.Stock-=1
            print("Book borrowed""\n""Current stock:",self.Stock)
        else:
            print("no stock available")

    def return_book(self):
        self.Stock+=1
        print(self.Title,"is returned")

    def current_stock(self):
        n=self.Stock
        print(n)
        return self.Stock

c1=library("The Red","JD",2)
c1.current_stock()

class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price

class cart():
    def __init__(self):
        self.products=[]

    def add(self,product):
        self.products.append(product)
        print(product.name,"added to the cart")

    def remove(self,product_name):
        for product in self.products:
            if product==product_name:
                self.products.remove(product_name)
                print(product_name.name,"is removed from the cart")
            else:
                print("not found")
    
    def total_price(self):
        s=0
        for product in self.products:
            s+=product.price
            print(s)
    def list(self):
        for product in self.products:
            print(product.name)
        
x1=Product("laptop",60000)
x2=Product("phone",15000)

mycart=cart()
