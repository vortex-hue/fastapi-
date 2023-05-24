from fastapi import FastAPI
from . import models
from  .database import engine
from sqlalchemy.orm import Session
from typing import List
from .route import blog, user, authentication 


# instatiate our app
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.route)
app.include_router(blog.router)
app.include_router(user.router)

