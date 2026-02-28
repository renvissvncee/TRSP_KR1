from fastapi import FastAPI

app = FastAPI()

@app.post("/calculate")
def calculate(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}