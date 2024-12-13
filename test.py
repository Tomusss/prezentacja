from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Dane połączenia
DATABASE_URL = "mysql+pymysql://student:57u>3n7@giniewicz.it:3306/sakila"

# Silnik połączenia
engine = create_engine(DATABASE_URL)

# Baza dla modeli
Base = declarative_base()

# Definicja modelu tabeli
class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    last_update = Column(DateTime)

# Utworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Pobranie i wyświetlenie danych
actors = session.query(Actor).all()
for actor in actors:
    print(f"ID: {actor.actor_id}, Imię: {actor.first_name}, Nazwisko: {actor.last_name}, Ostatnia aktualizacja: {actor.last_update}")

# Zamknięcie sesji
session.close()
engine.dispose()
