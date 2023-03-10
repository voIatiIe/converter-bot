"""added active field

Revision ID: ed1ffc30a18b
Revises: 755ce1b5555d
Create Date: 2023-01-31 00:44:38.369416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed1ffc30a18b'
down_revision = '755ce1b5555d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'active')
    # ### end Alembic commands ###
