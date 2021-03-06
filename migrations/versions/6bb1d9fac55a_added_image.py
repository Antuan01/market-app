"""added image

Revision ID: 6bb1d9fac55a
Revises: 173984b59d6f
Create Date: 2021-03-13 20:48:39.672576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bb1d9fac55a'
down_revision = '173984b59d6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imageable_id', sa.Integer(), nullable=False),
    sa.Column('imageable_type', sa.String(length=64), nullable=False),
    sa.Column('url', sa.String(length=850), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    # ### end Alembic commands ###
