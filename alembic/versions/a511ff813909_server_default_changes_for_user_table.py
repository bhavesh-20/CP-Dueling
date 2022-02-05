"""server default changes for user table

Revision ID: a511ff813909
Revises: 6089078909cd
Create Date: 2022-02-05 17:51:42.851942

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "a511ff813909"
down_revision = "6089078909cd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "is_active",
        existing_type=sa.BOOLEAN(),
        nullable=False,
        existing_server_default=sa.text("true"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "is_active",
        existing_type=sa.BOOLEAN(),
        nullable=True,
        existing_server_default=sa.text("true"),
    )
    # ### end Alembic commands ###
