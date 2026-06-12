# Pydantic is a data validation and data parsing library for python.It ensures that the data you work with is correct,structured and type-safe
from pydantic import BaseModel
class Student(BaseModel):
    name:str

newStudent = {'name' : 32}
student = Student(**newStudent)
print(student)