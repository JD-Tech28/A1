class student():
    name="JD"
    def __init__(self,subject,marks):
        self.subject=subject
        self.marks=marks

s1=student("Maths",95)
s2=student("science",95)
s3=student("social",95)

sum=(s1.marks+s2.marks+s3.marks)
avg=sum/3
print (student.name,":",avg)
print(avg)