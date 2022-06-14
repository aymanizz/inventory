"""create items table

Revision ID: d099ce6caf8e
Revises: 
Create Date: 2022-06-14 05:35:48.880028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd099ce6caf8e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit', sa.String(length=10), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('deletion_comment', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_name'), 'items', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_items_name'), table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###