from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/stociu_adresai.db')
Base = declarative_base()

class Stotis(Base):
    __tablename__ = "stotis"
    id = Column(Integer, primary_key = True)
    pavadinimas = Column("pavadinimas", String)
    tipas = Column("tipas", String)
    aljansas = Column("aljansas", String)
    korporacija = Column("korporacija", String)
    laikas = Column("laikas", Integer)
    datos = relationship("datos", back_populates = "stotis")

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas}, {self.tipas}, {self.aljansas}, {self.korporacija})"


class Puolejas(Base):
    __tablename__ = "puolejas"
    id = Column(Integer, primary_key = True)
    aljansas = Column("aljansas", String)
    korporacija = Column("korporacija", String)
    datos = relationship("datos", back_populates = "puolejas")

    def __repr__(self):
        return f"({self.id}, {self.aljansas}, {self.korporacija})"


class Regionas(Base):
    __tablename__ = "regionas"
    id = Column(Integer, primary_key = True)
    pavadinimas = Column("pavadinimas", String)

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas})"


class Dalyviai(Base):
    __tablename__ = "dalyviai"
    id = Column(Integer, primary_key = True)
    vardas = Column("vardas", String)
    ismoka = Column("ismoka", Integer)

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.ismoka})"


class Datos(Base):
    __tablename__ = "datos"
    id = Column(Integer, primary_key = True)
    apleidimo_laikas = Column("apleidimas", String)
    puolimo_laikas = Column("puolimas", String)
    stotis_id = Column(Integer, ForeignKey("stotis.id"))
    stotis = relationship("stotis", back_populates = "datos")
    puolejas_id = relationship(Integer, ForeignKey("puolejas.id"))
    puolejas = relationship("puolejas", back_populates = "datos")

    def __repr__(self):
        return f"({self.id}, {self.apleidimo_laikas}, {self.puolimo_laikas})"

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
