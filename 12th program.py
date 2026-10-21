student ={
"name":"Maqsood",
"age": 22,
"course":"Data Science"
}
print(student)
print(student.get("name"))
print(student["age"])
student["age"] = 23
student["city"] ="lahore"
student.pop("course") # remove course means data science 
print(student)
for key,value in student.items():
    print(key,":",value)