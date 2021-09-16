"""Initial migration

Revision ID: 281dcaed17d4
Revises: 
Create Date: 2021-09-02 12:31:15.045290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '281dcaed17d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Medida',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('proporcion', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Ingrediente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.Column('precio', sa.Float(), nullable=True),
    sa.Column('medida_id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['medida_id'], ['Medida.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Receta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.Column('precio_venta', sa.Float(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['Categoria.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('IngredienteReceta',
    sa.Column('receta_id', sa.Integer(), nullable=False),
    sa.Column('ingrediente_id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Float(), nullable=False),
    sa.Column('medida_id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ingrediente_id'], ['Ingrediente.id'], ),
    sa.ForeignKeyConstraint(['medida_id'], ['Medida.id'], ),
    sa.ForeignKeyConstraint(['receta_id'], ['Receta.id'], ),
    sa.PrimaryKeyConstraint('receta_id', 'ingrediente_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('IngredienteReceta')
    op.drop_table('Receta')
    op.drop_table('Ingrediente')
    op.drop_table('Medida')
    op.drop_table('Categoria')
    # ### end Alembic commands ###