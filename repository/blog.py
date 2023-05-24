from fastapi import Depends, Response, HTTPException, status
from typing import List
from .. import schema, models, database
from sqlalchemy.orm import Session
from ..repository import blog


get_db = database.get_db


def all(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schema.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, description=request.description, published=request.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Blog with the id {id} is not found in the Database")
    return blog

def destroy(id, db : Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Message': f'Blog with  id "{id}" is deleted'}


def update(id, request: schema.Blog,  db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update({'title': request.title, 'description': request.description, 'body': request.body, 'published': request.published}, synchronize_session='evaluate')
    if not blog:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'Blog with id {id} is not available in the database')
    db.commit()
    return {'message': f'{request.title} is updated successfully'}