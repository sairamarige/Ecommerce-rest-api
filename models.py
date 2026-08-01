from sqlalchemy import Column, Integer, String, Float
from database import Base

class Mobile(Base):
    __tablename__ = "mobiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    brand = Column(String(100))
    price = Column(Float)
    ram = Column(Integer)
    storage = Column(Integer)

class Laptop(Base):
    __tablename__ = "laptops"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    brand = Column(String(100))
    price = Column(Float)
    ram = Column(Integer)
    storage = Column(Integer)

class Tablet(Base):
    __tablename__ = "tablets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    brand = Column(String(100))
    price = Column(Float)
    storage = Column(Integer)

class SmartWatch(Base):
    __tablename__ = "smartwatches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    brand = Column(String(100))
    price = Column(Float)
    battery = Column(String(50))

class Headphone(Base):
    __tablename__ = "headphones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    brand = Column(String(100))
    price = Column(Float)
    wireless = Column(String(10))

