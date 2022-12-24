from peewee import * 
import datetime
import sys

db = SqliteDatabase("../../store/general_log.db")

class BaseModel(Model):
    class Meta:
        database = db

class OpenTrades(BaseModel):
    strategy = TextField(index=True)
    trade_id = TextField(unique=True)
    stock_symbol = TextField()
    stock_number = TextField()
    position = TextField()
    acq_price = DoubleField()
    acq_quantity = IntegerField()
    created_date = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        indexes = (
           (('strategy', 'stock_symbol'),False),
           (('strategy', 'stock_number'),False) 
        )

class GeneralLedger:
    strategy = TextField(index=True)
    trade_id = TextField()
    acq_price = DoubleField()
    release_price = DoubleField()
    acq_quantity = IntegerField()
    net_change = DoubleField()
    created_date = DateTimeField(default=datetime.datetime.now)