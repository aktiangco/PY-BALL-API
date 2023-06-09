"""empty message

Revision ID: 4a5f4e84c945
Revises: 077c9d4826e6
Create Date: 2023-05-12 10:54:10.294641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a5f4e84c945'
down_revision = '077c9d4826e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=250), nullable=True),
    sa.Column('scientific_name', sa.String(length=250), nullable=True),
    sa.Column('conservative_status', sa.String(length=250), nullable=True),
    sa.Column('native_habitat', sa.String(length=250), nullable=True),
    sa.Column('fun_fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reptiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('common_name', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('scientific_name', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('conservative_status', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('native_habitat', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('fun_fact', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='reptiles_pkey')
    )
    op.drop_table('reptile')
    # ### end Alembic commands ###
