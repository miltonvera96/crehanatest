from main import schema


def test_query(setup_database):
    query = """
        query TestQuery {
            posts {
                title
                body
            }
        }
    """

    result = schema.execute_sync(
        query
    )

    assert result.errors is None
    assert result.data["posts"] == [
        {
            "title": "The Great Gatsby",
            "body": "F. Scott Fitzgerald",
        }
    ]