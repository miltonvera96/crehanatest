from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .connection import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    title = Column(String, unique=True, index=True)
    body = Column(String, index=True)

    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    body = Column(String, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("Post", back_populates="comments")
