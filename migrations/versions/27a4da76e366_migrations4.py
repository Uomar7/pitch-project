"""migrations4

Revision ID: 27a4da76e366
Revises: f278a6a04029
Create Date: 2019-05-30 11:47:40.604764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27a4da76e366'
down_revision = 'f278a6a04029'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'pitches', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    # ### end Alembic commands ###