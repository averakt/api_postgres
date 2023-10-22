"""user FIO

Revision ID: c7ed0f899d96
Revises: 3f9e6ffcd7a5
Create Date: 2023-10-22 22:00:47.076648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7ed0f899d96'
down_revision = '3f9e6ffcd7a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'resource', ['brief'])
    op.add_column('users', sa.Column('first_name', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('patronymic', sa.String(length=100), nullable=True))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('users', 'patronymic')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_constraint(None, 'resource', type_='unique')
    # ### end Alembic commands ###