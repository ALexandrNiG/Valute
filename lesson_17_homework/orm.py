from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=True)
Base = declarative_base()


class Words(Base):
    __tablename__ = 'words'
    id = Column('id', Integer, primary_key=True)
    word = Column('word', String, unique=True)
    count = Column('count', Integer)
    up = Column('up', Integer)
    down = Column('down', Integer)

    def __init__(self, word, count, up, down):
        self.word = word
        self.count = count
        self.up = up
        self.down = down


    def __str__(self):
        return f'{self.id} | {self.word} | {self.count} | {self.up} | {self.down}'


class Skills(Base):
    __tablename__ = 'skills'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name,):
        self.name = name

    def __str__(self):
        return f'{self.id} | {self.name}'


class Wordskills(Base):
    __tablename__ = 'wordskills'
    id = Column('id', Integer, primary_key=True)
    id_word = Column('id_word', Integer, ForeignKey('words.id'))
    id_skill = Column('id_skill', Integer, ForeignKey('skills.id'))
    count = Column('count', Integer)
    percent = Column('percent', Integer)


    def __init__(self, id_word, id_skill, count, percent):
        self.id_word = id_word
        self.id_skill = id_skill
        self.count = count
        self.percent = percent
    def __str__(self):
        return f'{self.id} | {self.id_word} | {self.id_skill} | {self.count} | {self.percent}'

Base.metadata.create_all(engine)
