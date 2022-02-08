from typing import Optional
import strawberry
from database.models import Post as PostModel
from database.models import Comment as CommentModel


@strawberry.type
class Post:
    user_id: int
    title: str
    body: str
    id: Optional[int] = None


@strawberry.type
class Comment:
    post_id: int
    name: str
    email: str
    body: str
    id: Optional[int] = None


@strawberry.type
class Response:
    code: int
    success: bool
    message: str


@strawberry.type
class ResponsePost(Response):
    post: Optional[Post] = None


@strawberry.type
class ResponseComment(Response):
    comment: Optional[Comment] = None


def from_model_to_scheme_post(model: PostModel):
    return Post(id=model.id, user_id=model.user_id, title=model.title, body=model.body)


def from_model_to_scheme_comment(model: CommentModel):
    return CommentModel(id=model.id, email=model.email, name=model.name, body=model.body)
