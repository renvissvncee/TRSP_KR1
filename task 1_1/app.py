from fastapi import FastAPI

my_app = FastAPI()

@my_app.get("/")
def welcome():
    return {"message": "Авторелоад действительно работает"}
