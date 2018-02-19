from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import os

Base = declarative_base()
#THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#dbDataPath = 'sqlite:///'+os.path.join(THIS_FOLDER, 'gamecatalog.db')
dbDataPath = 'postgresql://catalog:catalog@localhost:5432/catalog'

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    game_item = relationship('GameItem', cascade='all, delete-orphan')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class GameItem(Base):
    __tablename__ = 'game_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    release_year = Column(String(4))
    platform = Column(String(50))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'release_year': self.release_year,
            'platform': self.platform,
        }


engine = create_engine(dbDataPath)


Base.metadata.create_all(engine)
