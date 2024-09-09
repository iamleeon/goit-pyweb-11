from sqlalchemy import Column, Integer, String, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    created_at = Column('created_at', DateTime, default=func.now())
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(320), nullable=False)
    phone = Column(String(15), nullable=False)
    birthday = Column("birthday", DateTime, nullable=False)
    additional_info = Column(String(150), nullable=True)
