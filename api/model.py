from sqlalchemy import Column, Integer, String, Text, Boolean, Numeric, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    username = Column(String(50), unique=True,nullable=False)       
    password = Column(Text, nullable=False)
    is_staff = Column(Boolean, default=False)
    telegram_id = Column(Integer, primary_key=True)


class Product(Base):
    __tablename__ = 'shop_product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    image = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    price = Column(Numeric(10, 2), nullable=False)
    price_type = Column(String(4))
    category_code = Column(String(100), nullable=False)
    category_name = Column(String(100), nullable=False)
    subcategory_code = Column(String(100), nullable=False)
    subcategory_name = Column(String(100), nullable=False)
    # date = Column(DateTime, default=datetime.utcnow, nullable=False)
    # telegram_id = Column(Integer, primary_key=True, nullable=False, unique=True)


class Cart(Base):
    __tablename__ = 'web_cart'

    id = Column(Integer, primary_key=True, index=True)
    title_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    last_update = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
