"""_Production tables hack

Revision ID: 4fad4b3e9f55
Revises: d3684fcdaf4c
Create Date: 2021-12-28 11:59:34.865952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fad4b3e9f55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
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
    # op.create_table('alembic_version',
    # sa.Column('version_num', sa.String(length=32), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('version_num', name='alembic_version_pkc')
    # )
    # op.create_table('User',
    # sa.Column('UserID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('UserProfileURL', sa.String(length=300, collation=None), autoincrement=False, nullable=True),
    # sa.Column('UserImageURL', sa.String(length=300, collation=None), autoincrement=False, nullable=True),
    # sa.Column('FirstName', sa.String(length=75), autoincrement=False, nullable=True),
    # sa.Column('LastNameInitial', sa.String(length=5), autoincrement=False, nullable=True),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('UserID', name='PK_User_UserID')
    # )
    # op.create_table('TransactionType',
    # sa.Column('TransactionID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('TransactionName', sa.String(length=100, collation=None), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('TransactionID', name='PK_TransactionType_TransactionID')
    # )
    # op.create_table('Country',
    # sa.Column('CountryID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('CountryName', sa.String(length=200), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('CountryID', name='PK_Country_CountryID')
    # )
    # op.create_table('State',
    # sa.Column('StateID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('StateName', sa.String(length=60, collation=None), autoincrement=False, nullable=True),
    # sa.Column('AbrvState', sa.String(length=10, collation=None), autoincrement=False, nullable=True),
    # sa.Column('CountryID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['CountryID'], ['Country.CountryID'], name='FK_State_Country', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('StateID', name='PK_State_StateID')
    # )
    # op.create_table('PaymentLevel',
    # sa.Column('PaymentLevelID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('PaymentLevelSymbol', sa.String(length=10), autoincrement=False, nullable=False),
    # sa.Column('PaymentLevelName', sa.String(length=15, collation=None), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('PaymentLevelID', name='PK_PaymentLevel_PaymentLevelID')
    # )
    # op.create_table('EventCategory',
    # sa.Column('EventCategoryID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('EventCategoryName', sa.String(length=80), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('EventCategoryID', name='PK_EventCategory_EventCategoryID')
    # )
    # op.create_table('County',
    # sa.Column('CountyID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('CountyName', sa.String(length=150, collation=None), autoincrement=False, nullable=False),
    # sa.Column('StateID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['StateID'], ['State.StateID'], name='FK_County_State', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('CountyID', name='PK_County_CountyID')
    # )
    # op.create_table('City',
    # sa.Column('CityID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('CityName', sa.String(length=200), autoincrement=False, nullable=False),
    # sa.Column('StateID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('CountyID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['CountyID'], ['County.CountyID'], name='FK_City_County'),
    # # sa.ForeignKeyConstraint(['StateID'], ['State.StateID'], name='FK_City_State', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('CityID', name='PK_City_CityID')
    # )
    # op.create_table('BusinessCategory',
    # sa.Column('CategoryID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('CategoryName', sa.String(length=100), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('CategoryID', name='PK_BusinessCategory_CategoryID')
    # )
    # op.create_table('Business',
    # sa.Column('BusinessID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('BusinessName', sa.String(length=100), autoincrement=False, nullable=True),
    # sa.Column('ChainName', sa.String(length=100), autoincrement=False, nullable=True),
    # sa.Column('AddressLine1', sa.String(length=150), autoincrement=False, nullable=True),
    # sa.Column('AddressLine2', sa.String(length=200, collation=None), autoincrement=False, nullable=True),
    # sa.Column('AddressLine3', sa.String(length=100, collation=None), autoincrement=False, nullable=True),
    # sa.Column('Latitude', sa.DECIMAL(precision=8, scale=6), autoincrement=False, nullable=True),
    # sa.Column('Longitude', sa.DECIMAL(precision=9, scale=6), autoincrement=False, nullable=True),
    # sa.Column('ZipCode', sa.String(length=40, collation=None), autoincrement=False, nullable=True),
    # sa.Column('BusinessPhone', sa.String(length=50), autoincrement=False, nullable=True),
    # sa.Column('BusinessURL', sa.String(length=500, collation=None), autoincrement=False, nullable=True),
    # sa.Column('is_closed', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('DistanceToCounty', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('CityID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('CountyID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('StateID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('PaymentLevelID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['CityID'], ['City.CityID'], name='FK_Business_City', ondelete='CASCADE'),
    # # sa.ForeignKeyConstraint(['CountyID'], ['County.CountyID'], name='FK_Business_County'),
    # # sa.ForeignKeyConstraint(['PaymentLevelID'], ['PaymentLevel.PaymentLevelID'], name='FK_Business_PaymentLevel', ondelete='CASCADE'),
    # # sa.ForeignKeyConstraint(['StateID'], ['State.StateID'], name='FK_Business_State'),
    # sa.PrimaryKeyConstraint('BusinessID', name='PK_Business_BusinessID')
    # )
    # # op.create_index('IX_Business_StateID', 'Business', ['StateID'], unique=False)
    # # op.create_index('IX_Business_PaymentLevelID', 'Business', ['PaymentLevelID'], unique=False)
    # # op.create_index('IX_Business_CountyID', 'Business', ['CountyID'], unique=False)
    # # op.create_index('IX_Business_CityID', 'Business', ['CityID'], unique=False)
    # # op.create_index('IX_Business_ChainName', 'Business', ['ChainName'], unique=False)
    
    # op.create_table('CountyGrowth',
    # sa.Column('CountyID', sa.INTEGER(),nullable=False),
    # sa.Column('EstimationYear', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('EstimatedPopulation', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('LastEditedWhen', sa.DATE(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['CountyID'], ['County.CountyID'], name='FK_CountyGrowth_County', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('CountyID', 'EstimationYear', name='PK_CountyGrowth_CountyID_EstimationYear')
    # )
    
    # # BusinessCategoryBridge did not work from here but it follows the same "template" as BusinessTransactionBridge
    # op.create_table('BusinessCategoryBridge',
    # sa.Column('BusinessID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('CategoryID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['BusinessID'], ['Business.BusinessID'], name='FK_BusinessCategoryBridge_Business', ondelete='CASCADE'),
    # # sa.ForeignKeyConstraint(['CategoryID'], ['.CategoryID'], name='FK_BusinessCategoryBridge_BusinessCategory', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('BusinessID', 'CategoryID', name='PK_BusinessCategoryBridge_BusinessID_CategoryID')
    # )
    
    
    
    # op.create_table('BusinessHolding',
    # sa.Column('BusinessHoldingID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('BusinessID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('BusinessRating', sa.NUMERIC(precision=2, scale=1), autoincrement=False, nullable=True),
    # sa.Column('ReviewCount', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('CloseDate', sa.DATE(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['BusinessID'], ['Business.BusinessID'], name='FK_BusinessHolding_Business', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('BusinessHoldingID', name='PK_BusinessHolding_BusinessHoldingID')
    # )
    # # op.create_index('IX_BusinessHolding_CloseDate_SalesYTD', 'BusinessHolding', ['CloseDate'], unique=False)
    # # op.create_index('IX_BusinessHolding_BusinessID_SalesYTD', 'BusinessHolding', ['BusinessID'], unique=False)

    # op.create_table('BusinessTransactionBridge',
    # sa.Column('BusinessID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('TransactionID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['BusinessID'], ['Business.BusinessID'], name='FK_BusinessTransactionBridge_Business', ondelete='CASCADE'),
    # # sa.ForeignKeyConstraint(['TransactionID'], ['TransactionType.TransactionID'], name='FK_BusinessTransactionBridge_TransactionType', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('BusinessID', 'TransactionID', name='PK_BusinessTransactionBridge_BusinessID_TransactionID')
    # )
    # op.create_table('Review',
    # sa.Column('ReviewID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('ReviewURL', sa.String(length=300, collation=None), autoincrement=False, nullable=True),
    # sa.Column('ReviewExtract', sa.String(length=350), autoincrement=False, nullable=True),
    # sa.Column('ReviewRating', sa.DECIMAL(precision=28, scale=0), autoincrement=False, nullable=True),
    # sa.Column('UserID', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('BusinessID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('CreatedAt', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # sa.Column('InsertedAt', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['BusinessID'], ['Business.BusinessID'], name='FK_Review_Business', ondelete='CASCADE'),
    # # sa.ForeignKeyConstraint(['UserID'], ['User.UserID'], name='FK_Review_User', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('ReviewID', name='PK_Review_ReviewID')
    # )
    
    
    # op.create_table('Event',
    # sa.Column('EventID', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    # sa.Column('BusinessID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('EventName', sa.String(length=400), autoincrement=False, nullable=True),
    # sa.Column('Attending', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('CostOfAttending', sa.NUMERIC(precision=16, scale=1), autoincrement=False, nullable=True),
    # sa.Column('is_free', sa.String(length=50, collation=None), autoincrement=False, nullable=True),
    # sa.Column('EventDescription', sa.String(length=400), autoincrement=False, nullable=True),
    # sa.Column('Interested', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    # sa.Column('CityID', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('latitude', sa.DECIMAL(precision=8, scale=6), autoincrement=False, nullable=True),
    # sa.Column('longitude', sa.DECIMAL(precision=9, scale=6), autoincrement=False, nullable=True),
    # sa.Column('ZipCode', sa.String(length=50), autoincrement=False, nullable=True),
    # sa.Column('StartTime', sa.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    # sa.Column('EndTime', sa.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    # sa.Column('TicketsUrl', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    # sa.Column('EventSiteUrl', sa.String(length=400, collation=None), autoincrement=False, nullable=True),
    # sa.Column('CancelDate', sa.DATE(), autoincrement=False, nullable=True),
    # sa.Column('OfficialDate', sa.DATE(), autoincrement=False, nullable=True),
    # sa.Column('CreatedAt', sa.DATE(), autoincrement=False, nullable=True),
    # sa.Column('LastEditedWhen', sa.TIMESTAMP(), autoincrement=False, nullable=False),
    # # sa.ForeignKeyConstraint(['BusinessID'], ['Business.BusinessID'], name='FK_Event_Business', ondelete='CASCADE'),
    # # sa.ForeignKeyConstraint(['CityID'], ['City.CityID'], name='FK_Event_City'),
    # sa.PrimaryKeyConstraint('EventID', name='PK_Event_EventID')
    # )


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
    
    
    
    
    
    
    
    
    
    
