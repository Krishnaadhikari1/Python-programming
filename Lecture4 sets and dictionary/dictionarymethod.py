#dictionary methods
student={
    "name":"Kiran ",
    "subjects":{
        "science":87,
        "maths":95,
        "english":89
    }
}
print(student)
print(student.keys())
print(len(student))
print(list(student.values()))
print(student.items())
print(student.get("name"))
student.update({"school":"jana jyoti "})
print(student)