"""changed default to server_default for is_active column of users table

Revision ID: 6089078909cd
Revises: e956e50dc089
Create Date: 2022-02-05 12:59:48.946826

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "6089078909cd"
down_revision = "e956e50dc089"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
