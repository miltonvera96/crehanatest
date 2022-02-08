import pytest
from main import schema
from database.handler_db import PostHandler
from database.models import Post


def mock_create_post(*args, **kwargs):
    return Post(id=1, title="The Great Gatsby", body="F. Scott Fitzgerald", user_id=1)


@pytest.mark.asyncio
async def test_mutation(monkeypatch):
    mutation = """
        mutation TestMutation($title: String!, $body: String!, $userId: Int!) {
          addPost(
            title: $title, body: $body, userId: $userId) {
            success
            message
            code
            post{
                id
                title
                userId
                body
            }
          }
        }
    """

    monkeypatch.setattr(PostHandler, "create", mock_create_post)

    resp = await schema.execute(
        mutation,
        variable_values={
            "userId": 1,
            "title": "The Great Gatsby",
            "body": "F. Scott Fitzgerald",
        },
    )

    assert resp.errors is None
    assert resp.data["addPost"] == {
        "success": True,
        "message": "Post created!",
        "code": 200,
        "post": {
            "id": 1,
            "userId": 1,
            "title": "The Great Gatsby",
            "body": "F. Scott Fitzgerald",
        }
    }
