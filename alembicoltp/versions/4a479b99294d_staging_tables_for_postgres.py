"""staging tables for postgres

Revision ID: 4a479b99294d
Revises: 69e8dc6f7dbd
Create Date: 2021-12-29 10:39:10.480147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a479b99294d'
down_revision = '4fad4b3e9f55'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Event',
    sa.Column('county', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('attending_count', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('category', sa.String(length=80, collation=None), autoincrement=False, nullable=True),
    sa.Column('cost', sa.String(length=80, collation=None), autoincrement=False, nullable=True),
    sa.Column('cost_max', sa.String(length=80, collation=None), autoincrement=False, nullable=True),
    sa.Column('description', sa.String(length=450), autoincrement=False, nullable=True),
    sa.Column('event_site_url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('id', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('interested_count', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('is_canceled', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('is_free', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('is_official', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('name', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('tickets_url', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('time_end', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('time_start', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('business_id', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address1', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('location address2', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address3', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location city', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('location zip_code', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('location country', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location state', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('location cross_streets', sa.String(length=400, collation=None), autoincrement=False, nullable=True)
    )
    op.create_table('Transactions',
    sa.Column('transaction', sa.String(length=100, collation=None), autoincrement=False, nullable=True),
    sa.Column('businessalias', sa.String(length=200), autoincrement=False, nullable=True),
    sa.Column('businessid', sa.String(length=100, collation=None), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True)
    )
    op.create_table('Review',
    sa.Column('id', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('text', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('rating', sa.DECIMAL(precision=28, scale=0), autoincrement=False, nullable=True),
    sa.Column('time_created', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('user id', sa.String(length=100, collation=None), autoincrement=False, nullable=True),
    sa.Column('user profile_url', sa.String(length=300, collation=None), autoincrement=False, nullable=True),
    sa.Column('user image_url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('user name', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('business_id', sa.String(length=200), autoincrement=False, nullable=True),
    sa.Column('business_alias', sa.String(length=200), autoincrement=False, nullable=True)
    )
    op.create_table('StateAbbreviations',
    sa.Column('Us_State', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('Postal_Abbreviation', sa.String(length=50, collation=None), autoincrement=False, nullable=True)
    )
    op.create_table('County2',
    sa.Column('POP', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('DATE_CODE', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('state', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('county', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('year', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True)
    )
    op.create_table('Review2',
    sa.Column('id', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('text', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('rating', sa.DECIMAL(precision=28, scale=0), autoincrement=False, nullable=True),
    sa.Column('time_created', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('user id', sa.String(length=100, collation=None), autoincrement=False, nullable=True),
    sa.Column('user profile_url', sa.String(length=300, collation=None), autoincrement=False, nullable=True),
    sa.Column('user image_url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('user name', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('business_id', sa.String(length=200), autoincrement=False, nullable=True),
    sa.Column('business_alias', sa.String(length=200), autoincrement=False, nullable=True)
    )
    op.create_table('categories2',
    sa.Column('alias', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('title', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('businessalias', sa.String(length=200), autoincrement=False, nullable=True),
    sa.Column('businessid', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True)
    )
    op.create_table('test_table',
    sa.Column('Us_State', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('Postal_Abbreviation', sa.String(length=50, collation=None), autoincrement=False, nullable=True)
    )
    op.create_table('StateAbbreviations2',
    sa.Column('Us_State', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('Postal_Abbreviation', sa.String(length=50, collation=None), autoincrement=False, nullable=True)
    )
    op.create_table('Event2',
    sa.Column('county', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('attending_count', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('category', sa.String(length=80, collation=None), autoincrement=False, nullable=True),
    sa.Column('cost', sa.String(length=80, collation=None), autoincrement=False, nullable=True),
    sa.Column('cost_max', sa.String(length=80, collation=None), autoincrement=False, nullable=True),
    sa.Column('description', sa.String(length=450), autoincrement=False, nullable=True),
    sa.Column('event_site_url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('id', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('interested_count', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('is_canceled', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('is_free', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('is_official', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('name', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('tickets_url', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('time_end', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('time_start', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('business_id', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address1', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('location address2', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address3', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location city', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('location zip_code', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('location country', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location state', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('location cross_streets', sa.String(length=400, collation=None), autoincrement=False, nullable=True)
    )
    op.create_table('County',
    sa.Column('POP', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True),
    sa.Column('DATE_CODE', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('state', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('county', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('year', sa.NUMERIC(precision=18, scale=0), autoincrement=False, nullable=True)
    )
    op.create_table('Categories',
    sa.Column('alias', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('title', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('businessalias', sa.String(length=200), autoincrement=False, nullable=True),
    sa.Column('businessid', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True)
    )
    op.create_table('transactions2',
    sa.Column('transaction', sa.String(length=100, collation=None), autoincrement=False, nullable=True),
    sa.Column('businessalias', sa.String(length=200), autoincrement=False, nullable=True),
    sa.Column('businessid', sa.String(length=100, collation=None), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True)
    )
    op.create_table('Business',
    sa.Column('id', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('alias', sa.String(length=300, collation=None), autoincrement=False, nullable=True),
    sa.Column('name', sa.String(length=300), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('is_closed', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('url', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('review_count', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('rating', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('price', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('phone', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('display_phone', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('distance', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('coordinates latitude', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('coordinates longitude', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address1', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('location address2', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address3', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location city', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('location zip_code', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('location country', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location state', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('county', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True)
    )
    op.create_table('Business2',
    sa.Column('id', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('alias', sa.String(length=300, collation=None), autoincrement=False, nullable=True),
    sa.Column('name', sa.String(length=300), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('is_closed', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('url', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('review_count', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('rating', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('price', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('phone', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('display_phone', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('distance', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('coordinates latitude', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('coordinates longitude', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address1', sa.String(length=500), autoincrement=False, nullable=True),
    sa.Column('location address2', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location address3', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location city', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('location zip_code', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('location country', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    sa.Column('location state', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    sa.Column('county', sa.String(length=100), autoincrement=False, nullable=True),
    sa.Column('time_extracted', sa.DATE(), autoincrement=False, nullable=True)
    )


def downgrade():
    op.drop_index('IX_Business_ChainName', table_name='Business')
    op.drop_index('IX_Business_CityID', table_name='Business')
    op.drop_index('IX_Business_CountyID', table_name='Business')
    op.drop_index('IX_Business_PaymentLevelID', table_name='Business')
    op.drop_index('IX_Business_StateID', table_name='Business')
    op.drop_index('IX_BusinessHolding_BusinessID_SalesYTD', table_name='BusinessHolding')
    op.drop_index('IX_BusinessHolding_CloseDate_SalesYTD', table_name='BusinessHolding')
    
    op.drop_table('Review')
    op.drop_table('Event')
    op.drop_table('BusinessTransactionBridge')
    op.drop_table('BusinessHolding')
    op.drop_table('BusinessCategoryBridge')
    op.drop_table('CountyGrowth')
    op.drop_table('Business')
    op.drop_table('BusinessCategory')

    
    op.drop_table('City')
    op.drop_table('County')
    op.drop_table('EventCategory')
    op.drop_table('PaymentLevel')
    op.drop_table('State')
    op.drop_table('Country')
    # op.drop_table('alembic_version')
    op.drop_table('TransactionType')
    op.drop_table('User')
