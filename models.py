from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    email= Column(String)
    password= Column(String)
    location= Column(String)
    
    blogs = relationship('Blog', back_populates='creator')


class Blog(Base):
    __tablename__ = "blog"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    description = Column(String)
    published = Column(Boolean)

    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='blogs')



