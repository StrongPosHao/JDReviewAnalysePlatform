"""empty message

Revision ID: 9ecb6e67bce1
Revises: 722d2ff0e417
Create Date: 2017-11-04 10:19:20.129000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9ecb6e67bce1'
down_revision = '722d2ff0e417'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('information', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('information')
    op.add_column('reviews', sa.Column('product_id', sa.String(length=10), nullable=True))
    op.create_foreign_key(None, 'reviews', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'product_id')
    op.create_table('information',
    sa.Column('id', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('body', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('os', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('CPU', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('memory', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('hard_disk', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('graphics_card', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('drive', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('screen', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('net', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('interface', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('Audio', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('input', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('other_dev', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('battery', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('size', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('feature', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('product')
    # ### end Alembic commands ###
