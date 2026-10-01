from pydantic import BaseModel


class TaskCreate(BaseModel):  #defines a shape called TaskCreatea
    title: str
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


