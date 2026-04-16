Word={
    "Table":("A piece of furniture","list of facts & figures"),
    "Cat":"A small animal",
}
# print(Word)
# print(len(Word))
# print(type(Word))

Set1={"Python","Java","C++","Python","Javascript","Java","Python","Java","C++","C"}
# print(len(Set1))

# Grade={}
# Grade.update({"Maths":input("Marks Scored:")})
# Grade.update({"Science":input("Marks Scored:")})
# Grade.update({"Social":input("Marks Scored:")})
# print(Grade)

Set2={9}
Set3={"9.0"}
# print(Set2.union(Set3))

student={
        "name":"JD",
        "subjects":{
        "Maths":98,
        "science":100,
        }
}
# print(student["subjects"]["Maths"])
# print(student["subjects"].keys())
# print(student.values())
# print(list(student.items()))
# print(student.get("name"))

Subjects={}
Subjects.update({"Maths":input("Maths Score:")})
Subjects.update({"Science":input("science Score:")})

print(Subjects)
pairs=list(Subjects)
print(pairs[1])