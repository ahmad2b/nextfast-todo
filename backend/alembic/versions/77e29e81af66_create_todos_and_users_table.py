"""create todos and users table

Revision ID: 77e29e81af66
Revises: 
Create Date: 2024-01-08 20:41:19.830434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "77e29e81af66"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        create table users (
           id serial primary key,
           username varchar(100) not null unique,
           password varchar(100) not null,
           created_at timestamp default current_timestamp  
        );
        create table todos (
           id serial primary key,
           title varchar(100) not null,
           description varchar(100) not null,
           completed boolean not null default false,
           owner_id int references users(id) on delete cascade
        );
        """
    )


def downgrade() -> None:
    op.execute("drop table users; drop table todos;")
