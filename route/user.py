from fastapi import APIRouter, Depends, status
from blog import schema, database
from sqlalchemy.orm import Session
from ..repository import user
from .. import oauth2
router = APIRouter(
    prefix="/user",
    tags=["User"]
)

get_db = database.get_db

## Creating Users
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ShowUser)
async def create_user(request: schema.User,  db : Session = Depends(get_db)):
    return user.create_user(request, db)


## get a useer by id
@router.get("/{id}", response_model=schema.ShowUser)
async def show_user(id,  db : Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return user.show_user(id, db)