"""empty message

Revision ID: 640c6be52cef
Revises: 
Create Date: 2020-01-02 22:37:39.067828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '640c6be52cef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('child_2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('left',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parent_1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parent_3',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('right',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('association',
    sa.Column('left_id', sa.Integer(), nullable=True),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['left_id'], ['left.id'], ),
    sa.ForeignKeyConstraint(['right_id'], ['right.id'], )
    )
    op.create_table('child_1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_1.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('child_3',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parent_3.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parent_2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['child_2.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parent_2')
    op.drop_table('child_3')
    op.drop_table('child_1')
    op.drop_table('association')
    op.drop_table('users')
    op.drop_table('right')
    op.drop_table('parent_3')
    op.drop_table('parent_1')
    op.drop_table('left')
    op.drop_table('child_2')
    # ### end Alembic commands ###
