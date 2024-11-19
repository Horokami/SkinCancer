from pydantic import BaseModel

class UserBase(BaseModel):
    login: str

class CreateUser(UserBase):
    password: str
    firstName: str
    lastName: str

class User(UserBase):
    id: int
    firstName: str
    lastName: str

    class Config:
        orm_mode = True
        from_attributes = True

class Login(BaseModel):
    login: str
    password: str
