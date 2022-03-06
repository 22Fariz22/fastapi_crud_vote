"""add content column to post table

Revision ID: d2164631300b
Revises: 1375ef237b40
Create Date: 2022-03-05 12:14:04.171308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2164631300b'
down_revision = '1375ef237b40'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
