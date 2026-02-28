from pydantic import BaseModel, Field, validator

class User(BaseModel):
    name: str
    age: int
    
class Feedback(BaseModel):
    name: str = Field(..., min_length=2,max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @validator('message')
    def false_message(cls, value):
        bad_words = ["кринж", "рофл", "вайб"]
        for word in bad_words:
            if word in value.lower():
                raise ValueError(f"Использование недопустимых слов")
        return value
        