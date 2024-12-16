"""Tabela para guardar publicacoes favoritas

Revision ID: ea88481aab3e
Revises: e63430140749
Create Date: 2024-12-16 11:22:10.355338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea88481aab3e'
down_revision = 'e63430140749'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorito',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('publicacao_id', sa.Integer(), nullable=False),
    sa.Column('data_favorito', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['publicacao_id'], ['publicacao.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorito')
    # ### end Alembic commands ###