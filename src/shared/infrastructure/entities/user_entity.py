from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from src.shared.infrastructure.entities.core_entity import CoreEntity

Base = declarative_base()

class User(CoreEntity, Base):
    __tablename__ = 'users'

    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
