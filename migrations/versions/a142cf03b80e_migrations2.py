"""migrations2

Revision ID: a142cf03b80e
Revises: 5e7e0e643cfe
Create Date: 2019-05-30 02:05:14.271996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a142cf03b80e'
down_revision = '5e7e0e643cfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('feedback', sa.String(length=255), nullable=True))
    op.drop_column('comments', 'opinion')
    op.add_column('profile_photos', sa.Column('photo_path', sa.String(), nullable=True))
    op.drop_column('profile_photos', 'pic_path')
    op.add_column('users', sa.Column('profile_photo_path', sa.String(), nullable=True))
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'profile_photo_path')
    op.add_column('profile_photos', sa.Column('pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('profile_photos', 'photo_path')
    op.add_column('comments', sa.Column('opinion', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('comments', 'feedback')
    # ### end Alembic commands ###
