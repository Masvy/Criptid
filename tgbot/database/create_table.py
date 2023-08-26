from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, VARCHAR

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)

    wallet = Column(VARCHAR(30), unique=True, nullable=True)
