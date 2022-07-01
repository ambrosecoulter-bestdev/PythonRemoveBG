"""New fields in the User model.

Revision ID: 66ecee586b9e
Revises: 1ad9e065242a
Create Date: 2021-09-08 00:23:17.927298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66ecee586b9e'
down_revision = '1ad9e065242a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
