"""Add difficulty column

Revision ID: ceb8281af059
Revises: 
Create Date: 2024-11-15 11:18:51.971468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceb8281af059'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workout_exercises')
    with op.batch_alter_table('exercise', schema=None) as batch_op:
        batch_op.add_column(sa.Column('difficulty', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('muscle_groups', sa.JSON(), nullable=False))
        batch_op.add_column(sa.Column('needs_additional_weight', sa.Boolean(), nullable=False))
        batch_op.drop_column('muscle_group')
        batch_op.drop_column('need_additional_weight')

    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.drop_column('muscle_group')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.add_column(sa.Column('muscle_group', sa.VARCHAR(length=100), nullable=False))

    with op.batch_alter_table('exercise', schema=None) as batch_op:
        batch_op.add_column(sa.Column('need_additional_weight', sa.BOOLEAN(), nullable=False))
        batch_op.add_column(sa.Column('muscle_group', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('needs_additional_weight')
        batch_op.drop_column('muscle_groups')
        batch_op.drop_column('difficulty')

    op.create_table('workout_exercises',
    sa.Column('workout_id', sa.INTEGER(), nullable=False),
    sa.Column('exercise_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['workout.id'], ),
    sa.PrimaryKeyConstraint('workout_id', 'exercise_id')
    )
    # ### end Alembic commands ###
