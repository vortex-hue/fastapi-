from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, models
from ..hash import Hash
from .token import create_access_token
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm


get_db = database.get_db

route = APIRouter(tags=["Authentication"])


ACCESS_TOKEN_EXPIRE_MINUTES = 30


@route.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(),  db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"user email '{request.email}' is not found in our database")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect Password!!")
    
    #Generate jwt and return it
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


