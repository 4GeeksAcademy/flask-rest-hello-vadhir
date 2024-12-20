"""create planet table

Revision ID: 651de5cd71ac
Revises: a5cffa318ac2
Create Date: 2024-12-02 06:33:50.219226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651de5cd71ac'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=250),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=255),
               nullable=True)

    op.drop_table('planet')
    # ### end Alembic commands ###
