import strawberry
from api.graphql.dataclasses import Post, Comment, ResponsePost, ResponseComment
from integration.exceptions import JPApiError
from integration.fake_data_api import FakeData
from database.handler_db import PostHandler, CommentHandler


@strawberry.type
class Mutation:

    # Create objects
    @strawberry.mutation
    def add_post(self, title: str, user_id: int, body: str) -> ResponsePost:
        api = FakeData()
        try:
            api.create_post({
                "title": title,
                "body": body,
                "userId": user_id
            })

            post = Post(title=title, user_id=user_id, body=body)
            new = PostHandler.create(post)
            post.id = new.id

            return ResponsePost(
                code=200, success=True, message="Post created!", post=post
            )
        except JPApiError as e:
            return ResponsePost(code=e.status_code, success=False, message="Error connecting to api!")

    @strawberry.mutation
    def add_comment(self, name: str, email: str, body: str, post_id: int) -> ResponseComment:
        try:
            comment = Comment(name=name, email=email, body=body, post_id=post_id)
            new = CommentHandler.create(comment, post_id)
            comment.id = new.id

            return ResponseComment(
                code=200, success=True, message="Comment created!", comment=comment
            )
        except Exception as e:
            return ResponseComment(code=400, success=False, message=str(e))

    # Update objects
    @strawberry.mutation
    def update_post(self, id: int, title: str, user_id: int, body: str) -> ResponsePost:
        try:
            post = Post(id=id, title=title, user_id=user_id, body=body)
            PostHandler.update(post)
            return ResponsePost(code=200, success=False, message="Post updated!", post=post)
        except Exception as e:
            return ResponsePost(code=400, success=False, message=str(e))

    @strawberry.mutation
    def update_comment(self, id: int, name: str, email: str, body: str, post_id: int) -> ResponseComment:
        try:
            comment = Comment(id=id, name=name, email=email, body=body, post_id=post_id)
            CommentHandler.update(comment)
            return ResponseComment(code=200, success=False, message="Comment updated!", comment=comment)
        except Exception as e:
            return ResponseComment(code=400, success=False, message=str(e))

    # Delete objects
    @strawberry.mutation
    def delete_post(self, id: int) -> ResponsePost:
        try:
            success = PostHandler.delete(id)
            return ResponsePost(code=204, success=success, message="Post deleted!")
        except Exception as e:
            return ResponsePost(code=400, success=False, message=str(e))

    @strawberry.mutation
    def delete_comment(self, id: int) -> ResponseComment:
        try:
            success = CommentHandler.delete(id)
            return ResponseComment(code=204, success=success, message="Comment deleted!")
        except Exception as e:
            return ResponseComment(code=400, success=False, message=str(e))

