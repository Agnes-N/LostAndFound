"""relation  Migration

Revision ID: cac0d74213a9
Revises: 9bf786d46ef3
Create Date: 2019-10-02 12:15:42.880223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac0d74213a9'
down_revision = '9bf786d46ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('found', sa.Column('lost_id', sa.Integer(), nullable=True))
    op.add_column('found', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'found', 'lost', ['lost_id'], ['id'])
    op.create_foreign_key(None, 'found', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'found', type_='foreignkey')
    op.drop_constraint(None, 'found', type_='foreignkey')
    op.drop_column('found', 'user_id')
    op.drop_column('found', 'lost_id')
    # ### end Alembic commands ###