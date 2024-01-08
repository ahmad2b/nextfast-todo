"""create todos table

Revision ID: ac87fe608488
Revises: 
Create Date: 2024-01-08 11:18:01.063700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ac87fe608488"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
               create table todos (
                   id serial primary key,
                   title varchar(100) not null,
                   description varchar(100) not null,
                   completed boolean not null default false
               )
        """
    )


def downgrade() -> None:
    op.execute("drop table todos;")
