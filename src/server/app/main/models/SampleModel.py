from app.main import db
import datetime
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

Base = declarative_base()
#one2many

class ParentModel_1(db.Model, Base):
    __tablename__ = 'parent_1'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(80), nullable=False)
    created_at = Column(db.DateTime(timezone=True),
                nullable=False, default=datetime.datetime.now())
    children = relationship("ChildModel_1")

class ChildModel_1(db.Model, Base):
    __tablename__ = 'child_1'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent_1.id'))

#many2one

class ParentModel_2(db.Model, Base):
    __tablename__ = 'parent_2'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child_2.id'))
    child = relationship("ChildModel_2")

class ChildModel_2(db.Model, Base):
    __tablename__ = 'child_2'
    id = Column(Integer, primary_key=True)

#one2one

class ParentModel_3(db.Model, Base):
    __tablename__ = 'parent_3'
    id = Column(Integer, primary_key=True)
    child = relationship("ChildModel_3", backref=backref("parent_3", uselist=False))

class ChildModel_3(db.Model, Base):
    __tablename__ = 'child_3'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent_3.id'))
    parent = relationship("ParentModel_3")

#many2many

association_table = Table('association', db.Model.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class ParentModel_4(db.Model):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("ChildModel_4",
                    secondary=association_table)

class ChildModel_4(db.Model):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)