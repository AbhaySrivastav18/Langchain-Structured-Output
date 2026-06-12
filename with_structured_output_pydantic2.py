# Pydantic is a data validation and data parsing library for python.It ensures that the data you work with is correct,structured and type-safe
from pydantic import BaseModel,EmailStr
from typing import Optional
class Student(BaseModel):
    name:str = 'Abhay'
    age : Optional[int] = None
    email : EmailStr

newStudent = {'age':32,'email':'abc'}
student = Student(**newStudent)
print(student)