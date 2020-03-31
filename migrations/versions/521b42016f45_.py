"""empty message

Revision ID: 521b42016f45
Revises: 
Create Date: 2020-03-25 22:27:38.916525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '521b42016f45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('twuser',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('screen_name', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('followers_count', sa.Integer(), nullable=True),
    sa.Column('latest_tweet_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tweet',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('full_text', sa.String(length=500), nullable=True),
    sa.Column('embedding', sa.PickleType(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['twuser.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    op.drop_table('twuser')
    # ### end Alembic commands ###