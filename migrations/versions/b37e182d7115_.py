"""empty message

Revision ID: b37e182d7115
Revises: 164d25ae2226
Create Date: 2017-12-04 09:07:18.279000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b37e182d7115'
down_revision = '164d25ae2226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('product_type', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'product_type')
    # ### end Alembic commands ###
