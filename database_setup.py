from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Catagory(Base):
    __tablename__ = 'catagory'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class Item(Base):
    __tablename__ = 'item'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    catagory_id = Column(Integer,ForeignKey('catagory.id'))
    catagory = relationship(Catagory)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
       }



engine = create_engine('sqlite:///itemcatalog.db')
 

Base.metadata.create_all(engine)
