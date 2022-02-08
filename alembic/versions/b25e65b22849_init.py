"""init

Revision ID: b25e65b22849
Revises: 
Create Date: 2022-02-07 16:12:06.739202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b25e65b22849'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String, primary_key=False),
        sa.Column('title', sa.String, primary_key=False),
        sa.Column('body', sa.String, primary_key=False)
    )

    op.create_table(
        "comments",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('post_id', sa.Integer, primary_key=False),
        sa.Column('name', sa.String, primary_key=False),
        sa.Column('email', sa.String, primary_key=False),
        sa.Column('body', sa.String, primary_key=False)
    )


def downgrade():
    op.drop_table('posts')
    op.drop_table('comments')
