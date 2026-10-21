student_list = [
    {"name":"Ali","age":18,"grade":"A"},
    {"name":"Sara","age":20,"grade":"B"},   
]
for student in student_list:
    print(f"Name: {student.get('name','')} | Grade:{student.get('grade','')}")
    