from fastapi import FastAPI, Path
from typing import Optional 
from pydantic import BaseModel 

app = FastAPI()

students = {
  1:{
    "name": "john",
    "age": 17,
    "year": "year 12"
  }
}

class Student(BaseModel):
  name: str
  age: int
  year: str
  
class UpdateStudent(BaseModel):
  name: Optional[str] = None 
  age : Optional[int] = None 
  year: Optional[str] = None 

names = {
  1: {
    "name": "first"
  },
  2:{
    "name": "second"
  }
}

@app.get("/")
def index():
  return {"name": "First Data"}


#Path parameter -> url/id or url/name 

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you wantt to view", gt=0)):
  return students[student_id]


@app.get("/get-name/{id}")
def get_name(id: int):
  return names[id]


#query param -> key value pair in the url ex -> google.com/results?search=Python 

@app.get("/get-by-name")
def get_student(*, name : Optional[str] = None, test:int):
  for id in students :
    if students[id]["name"] == name:
      return students[id]
  return {"Data": "Not found"}



#combining path ard quer param 
@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int, name : Optional[str] = None, test:int):
  for id in students :
    if students[id]["name"] == name:
      return students[id]
  return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student : Student):
  if student_id in students:
    return {"Error": "Student exists"}
  
  students[student_id] = student 
  return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int , student : UpdateStudent):
  if student_id not in students:
    return {"Error": "Student does not exists."}
  
  if student.name != None:
    students[student_id].name= student.name
    
  if student.age != None:
    students[student_id].age= student.age
    
  if student.year != None:
    students[student_id].year= student.year
    
  return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
  if student_id not in students:
    return {"Error": "Student doesn't exists"}
  
  del students[student_id]
  return {"Message": "Student Deleted successfully"}