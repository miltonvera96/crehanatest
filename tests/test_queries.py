from main import schema
from database.handler_db import PostHandler
from database.models import Post, Comment


def mock_get_posts(*args, **kwargs):
    return [
        Post(id=1, title="The Great Gatsby", body="F. Scott Fitzgerald", user_id=1)
    ]


def mock_get_post_comments(*args, **kwargs):
    return [
        Comment(id=1, email="scott@mail.com", name="F. Scott Fitzgerald", body="Amazing post", post_id=1)
    ]


def test_query_posts(monkeypatch):
    query = """
        query TestQuery {
            posts {
                id
                userId
                title
                body
                
            }
        }
    """

    monkeypatch.setattr(PostHandler, "get_all", mock_get_posts)
    result = schema.execute_sync(
        query,

    )

    assert result.errors is None
    assert result.data["posts"] == [
        {
            "id": 1,
            "userId": 1,
            "title": "The Great Gatsby",
            "body": "F. Scott Fitzgerald",
        }
    ]


def test_query_comments(monkeypatch):
    query = """
        query TestQuery($postId: Int!){
            commentsByPost(postId: $postId) {
                id
                email
                name
                body
            }
        }
    """

    monkeypatch.setattr(PostHandler, "get_comments", mock_get_post_comments)
    result = schema.execute_sync(
        query,
        variable_values={
            "postId": 1
        }
    )

    assert result.errors is None
    assert result.data["commentsByPost"] == [
        {
            "id": 1,
            "email": "scott@mail.com",
            "name": "F. Scott Fitzgerald",
            "body": "Amazing post"
        }
    ]