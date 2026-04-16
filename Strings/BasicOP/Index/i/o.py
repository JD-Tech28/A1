# f=open("guide.txt","w")
# f.write("i like Java\ni am programmimg in Java\ni am learning")
# f.close()

# f=open("guide.txt","r")
# data=f.read()
# newdata=data.replace("Java","Python")
# print(newdata)
# f.close()

# f=open("guide.txt","w")
# f.write(newdata)
# f.close()

# word="learning"
# with open("guide.txt","r")as f:
#     data=f.read()
#     if data.find(word) !=-1:
#         print("found")
#     else:
#         print("not found")

# with open("guide.txt","r")as f:
#     f.seek(0)       

# n="programmimg"
# i=1
# with open("guide.txt","r")as f:
#     while True:
#         data=f.readline()
#         if (n in data):
#             print("found at",i)
#         else:
#             i+=1
    
# with open("guide.txt","r") as f:
#     data = f.read()
#     f.seek(0)
#     print(data)

n = "programming"
i = 1
found = False

with open("guide.txt","r") as f:
    while True:
        data = f.readline()

        if not data:      # end of file
            break

        if n in data:
            print("found at line", i)
            found = True

        i += 1

if not found:
    print("not found")