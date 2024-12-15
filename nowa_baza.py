from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import random

#Silnik bazy danych (SQLite dla uproszczenia)
engine = create_engine("sqlite:///nowa_baza.db")

Base = declarative_base()

class Uzytkownik(Base):
    __tablename__ = 'uzytkownicy'
    id = Column(Integer, primary_key=True)
    imie = Column(String)
    email = Column(String)
    wiek = Column(Integer)
    
    zamowienia = relationship("Zamowienie", back_populates="uzytkownik")

class Zamowienie(Base):
    __tablename__ = 'zamowienia'
    id = Column(Integer, primary_key=True)
    uzytkownik_id = Column(Integer, ForeignKey('uzytkownicy.id'))
    id_produktu = Column(Integer)
    ilosc = Column(Integer)
    
    uzytkownik = relationship("Uzytkownik", back_populates="zamowienia")

#tworzenie tabel w bazie danych
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Generowanie losowych danych
def wypelnij_dane(liczba_uzytkownikow=10, liczba_zamowien=30):
    uzytkownicy = []
    for i in range(liczba_uzytkownikow):
        uzytkownik = Uzytkownik(
            imie=f"Uzytkownik{i}",
            email=f"uzytkownik{i}@poczta.com",
            wiek=random.randint(18, 80)
        )
        session.add(uzytkownik)
        uzytkownicy.append(uzytkownik)
    session.commit()

    for i in range(liczba_zamowien):
        zamowienie = Zamowienie(
            uzytkownik_id=random.choice(uzytkownicy).id,
            id_produktu=random.randint(1, 10),  
            ilosc=random.randint(1, 100) 
        )
        session.add(zamowienie)
    session.commit()

wypelnij_dane()

# Pobranie i wyświetlenie danych
print("Użytkownicy:")
for uzytkownik in session.query(Uzytkownik).all():
    print(uzytkownik.id, uzytkownik.imie, uzytkownik.email, uzytkownik.wiek)

print("\nZamówienia:")
for zamowienie in session.query(Zamowienie).all():
    print(zamowienie.id, zamowienie.uzytkownik_id, zamowienie.id_produktu, zamowienie.ilosc)

# Zamknięcie sesji
session.close()
engine.dispose()