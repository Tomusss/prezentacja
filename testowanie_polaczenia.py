from sqlalchemy import create_engine

# Konfiguracja połączenia
engine = create_engine("mysql+pymysql://student:57u>3n7@giniewicz.it:3306/sakila")

# Test połączenia
connection = engine.connect()
print("Połączenie z bazą danych zostało nawiązane!")
connection.close()