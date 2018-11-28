from sqlalchemy import create_engine, Column, Table, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base= declarative_base()

palavras_elementos= Table('palavras_elementos', Base.metadata,
    Column('palavras', Integer, ForeignKey('palavras.id')),
    Column('elemento', Integer, ForeignKey('elemento.id'))
)

class Palavras(Base):
    __tablename__ = 'palavras'
    id = Column(Integer, primary_key=True)
    pal = Column(String)
    elementos = relationship("Elemento",secondary=palavras_elementos,back_populates="palavras")

class Elemento(Base):
    __tablename__ = 'elemento'
    id = Column(Integer, primary_key=True)
    elem= Column(String)
    palavras = relationship("Palavras",secondary=palavras_elementos,back_populates="elementos")


engine= create_engine('sqlite:///spln1.db', echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

palavra = Palavras(pal="Bacon")
elemento = Elemento(elem="Ba")
elemento2=Elemento(elem="Co")
elemento3=Elemento(elem="N")
session.add_all([palavra,elemento,elemento2,elemento3])

palavra.elementos.append(elemento)
palavra.elementos.append(elemento2)
palavra.elementos.append(elemento3)

session.commit()

session.close()
