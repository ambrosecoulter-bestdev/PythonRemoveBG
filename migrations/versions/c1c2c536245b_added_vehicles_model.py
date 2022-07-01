"""Added vehicles model.

Revision ID: c1c2c536245b
Revises: 66ecee586b9e
Create Date: 2021-10-26 10:30:34.992344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1c2c536245b'
down_revision = '66ecee586b9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('make', sa.String(length=140), nullable=True),
    sa.Column('model', sa.String(length=140), nullable=True),
    sa.Column('year', sa.String(length=50), nullable=True),
    sa.Column('vin', sa.String(length=140), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('race_number', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    # ### end Alembic commands ###