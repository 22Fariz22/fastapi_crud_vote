"""add foreign-key to post table

Revision ID: d571f67307f4
Revises: 7debab584477
Create Date: 2022-03-05 13:32:39.960254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd571f67307f4'
down_revision = '7debab584477'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk', source_table = 'posts', referent_table = 'users',
                          local_cols = ['owner_id'], remote_cols = ['id'], ondelete = "CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name = 'posts')
    op.drop_column('posts', 'owner_id')
    pass
