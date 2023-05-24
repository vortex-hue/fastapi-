from pydantic import BaseModel
from typing import Optional, List




## Blog Model
class BlogBase(BaseModel):
    title: str
    description: str
    body: str
    published: Optional[bool]


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name : str
    email: str
    password: str
    location: str

class ShowUser(BaseModel):
    name: str
    email: str

    blogs: List[Blog] = []
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    description: str

    creator : ShowUser
    class Config:
        orm_mode = True

#token inheritancing
class Token(BaseModel):
    access_token: str
    token_type: str

#token data 
class TokenData(BaseModel):
    email: str | None = None

#login schema
class Login(BaseModel):
    email : str
    password : str