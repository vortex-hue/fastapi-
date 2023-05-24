from fastapi import APIRouter,  Depends, status
from typing import List
from .. import schema, database
from sqlalchemy.orm import Session
from ..repository import blog
from .. import oauth2

router = APIRouter(
    prefix='/blog',
    tags=["Blogs"]
)


get_db = database.get_db

# all blogs
@router.get("/", response_model=List[schema.ShowBlog])
async def all(db : Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
   return blog.all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog(request: schema.Blog, db : Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user) ):
    return blog.create(request, db)
  
## Get specific blog
@router.get("/{id}", response_model=schema.Blog)
async def show(id, db : Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)


#Delete the blog
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db : Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
   return blog.destroy(id, db)


#Update the blog
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: schema.Blog,  db : Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
   return blog.update(id, request,db)
