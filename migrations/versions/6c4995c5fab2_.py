"""empty message

Revision ID: 6c4995c5fab2
Revises: 33c35e557164
Create Date: 2023-01-22 21:12:41.869681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c4995c5fab2'
down_revision = '33c35e557164'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('institution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('institution', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_institution_address'), ['address'], unique=False)
        batch_op.create_index(batch_op.f('ix_institution_contact'), ['contact'], unique=False)
        batch_op.create_index(batch_op.f('ix_institution_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_institution_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('institution', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_institution_name'))
        batch_op.drop_index(batch_op.f('ix_institution_email'))
        batch_op.drop_index(batch_op.f('ix_institution_contact'))
        batch_op.drop_index(batch_op.f('ix_institution_address'))

    op.drop_table('institution')
    # ### end Alembic commands ###
