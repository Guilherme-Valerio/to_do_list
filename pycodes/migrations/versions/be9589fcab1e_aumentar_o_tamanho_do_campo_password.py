"""Aumentar o tamanho do campo password

Revision ID: be9589fcab1e
Revises: 
Create Date: 2024-10-14 15:42:47.188131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be9589fcab1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=128),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=512),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=512),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###
