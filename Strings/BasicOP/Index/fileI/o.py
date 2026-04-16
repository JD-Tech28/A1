
with open("D:\\jeevan D\\SMS Project\\Strings\\BasicOP\\Index\\pratice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")

with open("D:\\jeevan D\\SMS Project\\Strings\\BasicOP\\Index\\pratice.txt","w") as f:
    f.write(new_data)

word="learning"
with open("D:\\jeevan D\\SMS Project\\Strings\\BasicOP\\Index\\pratice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("not found")

def check_for_line():
    word="learning"
    data=True
    line_no =1
    with open("D:\\jeevan D\\SMS Project\\Strings\\BasicOP\\Index\\pratice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no+=1
    return -1

check_for_line()

count=1
with open("D:\\jeevan D\\SMS Project\\Strings\\BasicOP\\Index\\pratice.txt","r") as f:
    data=f.read()

    nums=data.split(",")
    for val1 in nums:
        if(int(val1)) % 2 ==0:
            count+=1

    print(count)