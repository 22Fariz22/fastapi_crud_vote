"""add last few column to post table

Revision ID: 7e43a68db31e
Revises: d571f67307f4
Create Date: 2022-03-06 02:01:51.435121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e43a68db31e'
down_revision = 'd571f67307f4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE',nullable=False)),
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True,
                                     server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
