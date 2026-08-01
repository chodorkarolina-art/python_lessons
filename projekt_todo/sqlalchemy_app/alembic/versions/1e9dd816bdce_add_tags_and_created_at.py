"""add tags and created_at

Revision ID: 1e9dd816bdce
Revises: c5f076971154
Create Date: 2026-05-24 19:39:40.069381

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e9dd816bdce'
down_revision: Union[str, Sequence[str], None] = 'c5f076971154'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        'tagi',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nazwa', sa.String(), nullable=False, unique=True)
    )

    op.create_table(
        'zadanie_tag',
        sa.Column('zadanie_id', sa.Integer(), nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['zadanie_id'], ['zadania.id']),
        sa.ForeignKeyConstraint(['tag_id'], ['tagi.id'])
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table('zadanie_tag')
    op.drop_table('tagi')
