"""Lost Migration

Revision ID: 84387f94891f
Revises: d9f797dd0248
Create Date: 2019-10-01 12:50:35.639675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84387f94891f'
down_revision = 'd9f797dd0248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lost_category'), 'lost', ['category'], unique=False)
    op.add_column('users', sa.Column('address', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'address')
    op.drop_index(op.f('ix_lost_category'), table_name='lost')
    op.drop_table('lost')
    # ### end Alembic commands ###