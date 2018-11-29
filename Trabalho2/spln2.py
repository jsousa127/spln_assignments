import re
import unicodedata
import html
from sys import argv
from sqlalchemy import create_engine, Column, Table, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

def lookup(word,pal):
    global array
    if not word:
        return 0
    a = session.query(Elemento)
    for e in a:
        el = e.elem.lower()
        if re.match(el, word) :
            if (len(word) == len(el)) | (lookup(word[len(el):],pal) == 1):
                pal.elementos.append(e)
                return 1

    return 0

def strip_accents(word):
   return ''.join(c for c in unicodedata.normalize('NFD', word)
                  if unicodedata.category(c) != 'Mn')

def populate_elements():
    elements = open("elements.txt","r").read().split()
    for e in elements:
        session.add(Elemento(elem=e))

Base= declarative_base()

class Palavras(Base):
    __tablename__ = 'palavras'
    id = Column(Integer, primary_key=True)
    pal = Column(String)
    elementos = relationship("Elemento",secondary=palavras_elementos)

class Elemento(Base):
    __tablename__ = 'elemento'
    id = Column(Integer, primary_key=True)
    elem= Column(String)

palavras_elementos= Table('palavras_elementos', Base.metadata,
    Column('palavras', Integer, ForeignKey('palavras.id')),
    Column('elemento', Integer, ForeignKey('elemento.id'))
)

engine= create_engine('sqlite:///spln.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
populate_elements()

f = open(argv[1],"r")
try:
    words = f.read().split()
except:
    try:
        import codecs
        words = codecs.open(argv[1],"r","iso-8859-1").read().split()
    except:
        print("Não foi possivel abrir o ficheiro")

for w in words:
    word = w.lower()
    pal = Palavras(pal=word)
    if lookup(word,pal):
        session.add(pal)

session.commit()
session.close()
