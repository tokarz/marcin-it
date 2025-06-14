import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import execute_values
import time

def stworz_baze_danych_sport():
    host = "localhost"
    user = "postgres"
    password = "admin"

    # 1. Tworzymy bazę danych Sport
    try:
        connection = psycopg2.connect(
            host=host,
            database="postgres",
            user=user,
            password=password
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname='sport'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE sport"))
            print("Baza danych 'sport' została utworzona.")
        else:
            print("Baza danych 'sport' już istnieje.")

    except Exception as error:
        print(f"Błąd podczas tworzenia bazy danych: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()

    # 2. Odczekaj chwilę, żeby baza zdążyła się utworzyć
    time.sleep(2)

    # 3. Łączymy się do nowo utworzonej bazy i tworzymy tabele oraz wstawiamy dane
    try:
        connection = psycopg2.connect(
            host=host,
            database="sport",
            user=user,
            password=password
        )
        cursor = connection.cursor()

        create_tables_sql = """
        CREATE TABLE IF NOT EXISTS Kluby (
            klub_id SERIAL PRIMARY KEY,
            nazwa VARCHAR(100) NOT NULL,
            miasto VARCHAR(100),
            stadion VARCHAR(100),
            rok_zalozenia INT
        );

        CREATE TABLE IF NOT EXISTS Rozgrywki (
            rozgrywka_id SERIAL PRIMARY KEY,
            nazwa VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Mecze (
            mecz_id SERIAL PRIMARY KEY,
            data_meczu DATE NOT NULL,
            klub_gospodarz_id INT NOT NULL,
            klub_gosc_id INT NOT NULL,
            wynik_gospodarz INT DEFAULT NULL,
            wynik_gosc INT DEFAULT NULL,
            stadion VARCHAR(100),
            rozgrywka_id INT NOT NULL,
            FOREIGN KEY (klub_gospodarz_id) REFERENCES Kluby(klub_id),
            FOREIGN KEY (klub_gosc_id) REFERENCES Kluby(klub_id),
            FOREIGN KEY (rozgrywka_id) REFERENCES Rozgrywki(rozgrywka_id)
        );

        CREATE TABLE IF NOT EXISTS Trenerzy (
            trener_id SERIAL PRIMARY KEY,
            imie VARCHAR(50) NOT NULL,
            nazwisko VARCHAR(50) NOT NULL,
            data_urodzenia DATE,
            narodowosc VARCHAR(50),
            klub_id INT,
            FOREIGN KEY (klub_id) REFERENCES Kluby(klub_id)
        );

        CREATE TABLE IF NOT EXISTS Pilkarze (
            pilkarz_id SERIAL PRIMARY KEY,
            imie VARCHAR(50) NOT NULL,
            nazwisko VARCHAR(50) NOT NULL,
            data_urodzenia DATE,
            narodowosc VARCHAR(50),
            pozycja VARCHAR(50),
            klub_id INT,
            FOREIGN KEY (klub_id) REFERENCES Kluby(klub_id)
        );

        CREATE TABLE IF NOT EXISTS Historia (
            historia_id SERIAL PRIMARY KEY,
            historia VARCHAR(1000),
            klub_id INT
        );
        """

        cursor.execute(create_tables_sql)
        connection.commit()
        print("Tabele zostały utworzone pomyślnie.")

        
    except Exception as error:
        print(f"Błąd podczas tworzenia tabel lub dodawania danych: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
