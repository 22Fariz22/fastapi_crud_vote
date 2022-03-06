"""add user table

Revision ID: 7debab584477
Revises: d2164631300b
Create Date: 2022-03-05 12:36:48.674600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7debab584477'
down_revision = 'd2164631300b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('email', sa.String, nullable=False),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
