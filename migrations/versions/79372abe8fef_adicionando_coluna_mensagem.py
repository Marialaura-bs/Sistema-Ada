from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '79372abe8fef'
down_revision = '1ee48ce89466'
branch_labels = None
depends_on = None

def upgrade():
    # Criação da nova tabela 'mensagens'
    op.create_table('mensagens',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('mensagem', sa.String(length=500), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id')
    )
    
    # Remover a tabela 'mensagens' anterior, caso tenha sido criada com o nome 'Mensagens'
    op.drop_table('mensagens')

def downgrade():
    # Reverter para a tabela 'Mensagens'
    op.create_table('Mensagens',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('name', sa.VARCHAR(length=100), nullable=False),
        sa.Column('email', sa.VARCHAR(length=100), nullable=False),
        sa.Column('senha', sa.VARCHAR(length=100), nullable=False),
        sa.Column('is_admin', sa.BOOLEAN(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('id')
    )
    
    # Remover a tabela 'mensagens' criada
    op.drop_table('mensagens')
