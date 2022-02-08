import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from database.connection import Base
from database.models import Post, Comment


@pytest.fixture(scope="session")
def connection():
    engine = create_engine(
        "postgresql://test_user:test_ppass@localhost/test_crehana"
    )
    return engine.connect()


def seed_database():
    posts = [
        {
            "id": 1,
            "title": "title for test",
            "body": "body for test",
            "user_id": 1,

        },
        # ...
    ]

    comments = [
        {
            "id": 1,
            "name": "Milton Vera",
            "email": "miltonvera96@gamil.com",
            "body": "body for test",
            "post_id": 1
        },
        # ...
    ]

    for post in posts:
        db_user = Post(**post)
        db_session.add(db_user)

    for comment in comments:
        db_user = Comment(**comment)
        db_session.add(db_user)
    db_session.commit()


@pytest.fixture(scope="module")
def setup_database(connection):
    Base.metadata.bind = connection
    Base.metadata.create_all()

    seed_database()

    yield

    Base.metadata.drop_all()


@pytest.fixture
def db_session(setup_database, connection):
    transaction = connection.begin()
    yield scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=connection)
    )
    transaction.rollback()
