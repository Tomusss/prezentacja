from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
# Silnik połączenia
engine = create_engine("mysql+pymysql://student:57u>3n7@giniewicz.it:3306/sakila")

# Baza dla modeli
Base = declarative_base()

# Definicja modelu tabeli
class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    last_update = Column(DateTime)

class Film_actor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(Integer, primary_key=True)
    film_id = Column(Integer, primary_key=True)
    last_update = Column(DateTime)
# Utworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Pobranie i wyświetlenie danych
actors = session.query(Actor).all()
for actor in actors:
    print(actor.actor_id, actor.first_name, actor.last_name, actor.last_update)

print('------------------')

actors_olivier = session.query(Actor).filter_by(last_name='olivier').all()
for actor in actors_olivier:
    print(f"ID: {actor.actor_id}, Imię: {actor.first_name}, Nazwisko: {actor.last_name}")


"""actor_films_count = (
    session.query(Actor.first_name, Actor.last_name, func.count(Film_actor.film_id).label("film_count"))
    .join(Film_actor, Actor.actor_id == Film_actor.actor_id)
    .group_by(Actor.actor_id)
    .order_by(func.count(Film_actor.film_id).desc())
    .all()
)"""
# Zamknięcie sesji
session.close()
engine.dispose()

"""# Przetwarzanie danych do wykresu
actor_names = [f"{actor.first_name} {actor.last_name}" for actor in actor_films_count]
film_counts = [actor.film_count for actor in actor_films_count]

plt.figure(figsize=(12, 6))
plt.bar(actor_names, film_counts, color='skyblue')
plt.xlabel("Aktorzy")
plt.ylabel("Liczba filmów")
plt.title("Liczba filmów, w których zagrał każdy aktor")
plt.xticks(rotation=90) 
plt.tight_layout()

plt.show()"""
