from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from calculator import *

app = FastAPI()

# Enable CORS for direct frontend files testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    a: float
    b: float

class Angle(BaseModel):
    angle: float

class ExpressionData(BaseModel):
    expression: str

@app.post('/add')
def addition(data: InputData):
    return {"result": add(data.a, data.b)}

@app.post('/subtract')
def subtraction(data: InputData):
    return {"result": subtract(data.a, data.b)}

@app.post('/multiply')
def multiplication(data: InputData):
    return {"result": multiply(data.a, data.b)}

@app.post('/divide')
def division(data: InputData):
    try:
        return {"result": divide(data.a, data.b)}
    except ValueError as e:
        return {"result": str(e)}

@app.post("/sin")
def calculate_sin(data: Angle):
    return {"result": sin(data.angle)}

@app.post("/cos")
def calculate_cos(data: Angle):
    return {"result": cos(data.angle)}

@app.post("/tan")
def calculate_tan(data: Angle):
    return {"result": tan(data.angle)}

@app.post("/calculate")
def calculate_expression(data: ExpressionData):
    try:
        res = safe_eval(data.expression)
        return {"result": res}
    except Exception as e:
        return {"result": "Invalid"}

# Mount frontend files at / after all API routes
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

