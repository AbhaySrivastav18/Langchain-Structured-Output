# Pydantic is a data validation and data parsing library for python.It ensures that the data you work with is correct,structured and type-safe
from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str = 'Abhay'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt = 0, lt = 10,default = 5,description="A decimal Value representing th cgpa of the student")

newStudent = {'age':32,'email':'abc','cgpa':9}
student = Student(**newStudent)
studentDict = dict(student)
print(studentDict['age'])