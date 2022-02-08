from . import models
from api.graphql.dataclasses import Post as PostScheme
from api.graphql.dataclasses import Comment as CommentScheme
from .connection import SessionLocal


class PostHandler:

    db = SessionLocal()

    @classmethod
    def get(cls, post_id: int):
        return cls.db.query(models.Post).get(post_id)

    @classmethod
    def get_all(cls, skip: int = 0, limit: int = 100):
        return cls.db.query(models.Post).offset(skip).limit(limit)

    @classmethod
    def get_comments(cls, post_id: int):
        return cls.db.query(models.Comment).filter(models.Comment.post_id == post_id)

    @classmethod
    def create(cls, post: PostScheme):
        db_post = models.Post(
            user_id=post.user_id, title=post.title, body=post.body
        )
        cls.db.add(db_post)
        cls.db.commit()
        cls.db.refresh(db_post)
        return db_post

    @classmethod
    def delete(cls, post_id: int):
        post = cls.db.query(models.Post).get(post_id)
        cls.db.delete(post)
        cls.db.commit()
        return True

    @classmethod
    def update(cls, post: PostScheme):
        current_post = cls.db.query(models.Post).get(post.id)
        current_post.user_id = post.user_id
        current_post.title = post.title
        current_post.body = post.body
        cls.db.add(current_post)
        cls.db.commit()

        return post


class CommentHandler:

    db = SessionLocal()

    @classmethod
    def get_all(cls, skip: int = 0, limit: int = 100):
        return cls.db.query(models.Comment).offset(skip).limit(limit)

    @classmethod
    def create(cls, comment: CommentScheme, post_id: int):
        db_comment = models.Comment(
            email=comment.email, name=comment.name, body=comment.body, post_id=post_id
        )
        cls.db.add(db_comment)
        cls.db.commit()
        cls.db.refresh(db_comment)
        return db_comment

    @classmethod
    def delete(cls, comment_id: int):
        comment = cls.db.query(models.Comment).get(comment_id)
        cls.db.delete(comment)
        cls.db.commit()
        return True

    @classmethod
    def update(cls, comment: CommentScheme):
        current_comment = cls.db.query(models.Comment).get(comment.id)
        current_comment.name = comment.name
        current_comment.email = comment.email
        current_comment.body = comment.body
        cls.db.add(current_comment)
        cls.db.commit()

        return comment
