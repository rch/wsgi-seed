import sqlalchemy as sqla
from sqlalchemy import Column, String, Integer, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship, backref
from . import bp, Base


class Entries(Base):
    __tablename__ = 'admin_entries'    
    id = Column('id_entries', Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    content = Column(String, nullable=False)
    updated = Column(DateTime, nullable=False)
    created = Column(DateTime, nullable=False)
