"""add release_time string

Revision ID: 7ac683c15aa8
Revises: 7e1bff3bd909
Create Date: 2018-01-17 09:32:28.248698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ac683c15aa8'
down_revision = '7e1bff3bd909'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('release_time', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'release_time')
    # ### end Alembic commands ###