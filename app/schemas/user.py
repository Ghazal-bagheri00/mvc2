from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    is_admin: bool = False

class UserOut(BaseModel):
    username: str
    is_admin: bool

class Token(BaseModel):
    access_token: str
    token_type: str
