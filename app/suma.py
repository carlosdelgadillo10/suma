#Suma
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Operacion(BaseModel):
    num1: float
    num2: float

# Endpoint para la operación de suma
@app.post("/sumar")
def sumar(op: Operacion):
    return op.num1 + op.num2

@app.post("/restar")
def restar(op: Operacion):
    return op.num1 - op.num2