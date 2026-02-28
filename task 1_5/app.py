from fastapi import FastAPI
from models import User

app = FastAPI()

@app.post("/user")
def userInfo(user: User):
    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}