import strawberry
from api.graphql.dataclasses import from_model_to_scheme_comment, from_model_to_scheme_post, Post, Comment
from database.handler_db import PostHandler, CommentHandler
import typing as t


@strawberry.type
class Query:

    @strawberry.field
    def posts(self) -> t.List[Post]:
        posts = PostHandler.get_all()
        return [from_model_to_scheme_post(p) for p in posts]

    @strawberry.field
    def post(self, post_id: int) -> Post:
        post = PostHandler.get(post_id)
        return from_model_to_scheme_post(post)

    @strawberry.field
    def comments(self) -> t.List[Comment]:
        posts = CommentHandler.get_all()
        return [from_model_to_scheme_comment(p) for p in posts]

    @strawberry.field
    def comments_by_post(self, post_id:int) -> t.List[Comment]:
        posts = PostHandler.get_comments(post_id)
        return [from_model_to_scheme_comment(p) for p in posts]
