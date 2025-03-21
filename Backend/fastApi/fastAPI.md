# FastAPI
It is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

# Installation
in cmd / virtual env:
python -m pip install fastapi

pip install uvicorn (uvicorn is used to run web server)

to run the app on server :
uvicorn appname:app --reload 


# API Syntax

Normal api ->  
```python
@app.get("/")
def index():
  return {"name": "First Data"}
```

# Path parameter -> 
ex-> url/id or url/name 


```python
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you wantt to view", gt=0, lt=2):
  return students[student_id] 
```

# Query param -> 
key value pair in the url ex -> google.com/results?search=Python 

```python
from typing import Optional 

@app.get("/get-by-name")
def get_student(*, name : Optional[str] = None, test:int):
  for id in students :
    if students[id]["name"] == name:
      return students[id]
  return {"Data": "Not found"}
```


# Passing req body 

```python 
from pydantic import BaseModel 

```


# Path module 
use Path to keep a check on path params like, default value , description , gt, lt , ge etc


```Python
from fastapi import FastAPI, Path

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you wantt to view", gt=0, lt=2)):
  return students[student_id]
```