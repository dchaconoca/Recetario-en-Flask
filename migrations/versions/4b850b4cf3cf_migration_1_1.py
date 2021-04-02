"""Migration 1.1

Revision ID: 4b850b4cf3cf
Revises: 67d0970cea95
Create Date: 2021-03-09 11:39:25.177736

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4b850b4cf3cf'
down_revision = '67d0970cea95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('Categoria',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('nombre', sa.String(length=50), nullable=False),
    # sa.Column('descripcion', sa.String(length=100), nullable=True),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('Medida',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('nombre', sa.String(length=50), nullable=False),
    # sa.Column('proporcion', sa.Float(), nullable=False),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('Ingrediente',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('nombre', sa.String(length=50), nullable=False),
    # sa.Column('descripcion', sa.String(length=100), nullable=True),
    # sa.Column('precio', sa.Float(), nullable=True),
    # sa.Column('medida_id', sa.Integer(), nullable=False),
    # sa.Column('created', sa.DateTime(), nullable=True),
    # sa.Column('updated', sa.DateTime(), nullable=True),
    # sa.ForeignKeyConstraint(['medida_id'], ['Medida.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    # op.create_table('Receta',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('titulo', sa.String(length=50), nullable=False),
    # sa.Column('descripcion', sa.Text(), nullable=True),
    # sa.Column('categoria_id', sa.Integer(), nullable=False),
    # sa.Column('precio_venta', sa.Float(), nullable=True),
    # sa.Column('created', sa.DateTime(), nullable=True),
    # sa.Column('updated', sa.DateTime(), nullable=True),
    # sa.ForeignKeyConstraint(['categoria_id'], ['Categoria.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
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
    op.drop_table('receta')
    op.drop_table('ingrediente')
    op.drop_table('categoria')
    op.drop_table('medida')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('medida',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(collation='latin1_spanish_ci', length=50), nullable=False),
    sa.Column('proporcion', mysql.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='latin1_spanish_ci',
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    op.create_table('categoria',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(collation='latin1_spanish_ci', length=50), nullable=False),
    sa.Column('descripcion', mysql.VARCHAR(collation='latin1_spanish_ci', length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='latin1_spanish_ci',
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    op.create_table('ingrediente',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(collation='latin1_spanish_ci', length=50), nullable=False),
    sa.Column('descripcion', mysql.VARCHAR(collation='latin1_spanish_ci', length=100), nullable=True),
    sa.Column('precio', mysql.FLOAT(), nullable=True),
    sa.Column('medida_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('created', mysql.DATETIME(), nullable=True),
    sa.Column('updated', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='latin1_spanish_ci',
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    op.create_table('receta',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('titulo', mysql.VARCHAR(collation='latin1_spanish_ci', length=50), nullable=False),
    sa.Column('descripcion', mysql.TEXT(collation='latin1_spanish_ci'), nullable=True),
    sa.Column('categoria_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('precio_venta', mysql.FLOAT(), nullable=True),
    sa.Column('created', mysql.DATETIME(), nullable=True),
    sa.Column('updated', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='latin1_spanish_ci',
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    op.drop_table('IngredienteReceta')
    op.drop_table('Receta')
    op.drop_table('Ingrediente')
    op.drop_table('Medida')
    op.drop_table('Categoria')
    # ### end Alembic commands ###
