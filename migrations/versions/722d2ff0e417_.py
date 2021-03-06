"""empty message

Revision ID: 722d2ff0e417
Revises: 
Create Date: 2017-10-29 23:29:48.691000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '722d2ff0e417'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('information',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('body', sa.String(length=200), nullable=False),
    sa.Column('os', sa.String(length=50), nullable=False),
    sa.Column('CPU', sa.String(length=200), nullable=False),
    sa.Column('memory', sa.String(length=200), nullable=False),
    sa.Column('hard_disk', sa.String(length=100), nullable=False),
    sa.Column('graphics_card', sa.String(length=200), nullable=False),
    sa.Column('drive', sa.String(length=100), nullable=False),
    sa.Column('screen', sa.String(length=200), nullable=False),
    sa.Column('net', sa.String(length=100), nullable=False),
    sa.Column('interface', sa.String(length=100), nullable=False),
    sa.Column('Audio', sa.String(length=100), nullable=False),
    sa.Column('input', sa.String(length=100), nullable=False),
    sa.Column('other_dev', sa.String(length=100), nullable=False),
    sa.Column('battery', sa.String(length=100), nullable=False),
    sa.Column('size', sa.String(length=100), nullable=False),
    sa.Column('feature', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('telephone', sa.String(length=11), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('reviews')
    op.drop_table('information')
    # ### end Alembic commands ###
