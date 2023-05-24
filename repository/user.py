from fastapi import APIRouter, Depends, Response, HTTPException, status
from typing import List
from blog import schema, models, database
from sqlalchemy.orm import Session
from ..hash import Hash


get_db = database.get_db

## Creating Users
def create_user(request: schema.User,  db : Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password), location=request.location)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


## get a useer by id
def show_user(id,  db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user id '{id}' is not found in our database")
    return user