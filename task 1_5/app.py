from fastapi import FastAPI
from models import User, Feedback

app = FastAPI()

@app.post("/user")
def userInfo(user: User):
    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}

feedbacks = []
@app.post("/feedback")
def addFeedback(feedback: Feedback):
    if ("всё плохо" in feedback.message.lower()):
        return "Ошибка добавления отзыва"
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
