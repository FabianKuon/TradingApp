from sqlalchemy import Sequence, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class StockModel(Base):
    __tablename__ = "stock_prices"
    stock_id_seq = Sequence('cart_id_seq', metadata=Base.metadata)
    stock_id = Column(Integer, stock_id_seq, server_default=stock_id_seq.next_value(), primary_key=True)
    wkn = Column(String(6))
    price = Column(Float)
    time_stamp = Column(DateTime)
