from fastapi import FastAPI
from models import User

app = FastAPI()

@app.post("/calculate")
def calculate(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}


user: User = User(name="Druzhinin Artem", id=1)
@app.get("/users")
def userInfo():
    return {"name": user.name, "id": user.id}