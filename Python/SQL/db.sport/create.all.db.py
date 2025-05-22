import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import execute_values
import time

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

    CREATE TABLE IF NOT EXISTS Mecze (
        mecz_id SERIAL PRIMARY KEY,
        data_meczu DATE NOT NULL,
        klub_gospodarz_id INT NOT NULL,
        klub_gosc_id INT NOT NULL,
        wynik_gospodarz INT DEFAULT NULL,
        wynik_gosc INT DEFAULT NULL,
        stadion VARCHAR(100),
        FOREIGN KEY (klub_gospodarz_id) REFERENCES Kluby(klub_id),
        FOREIGN KEY (klub_gosc_id) REFERENCES Kluby(klub_id)
    );
    """

    cursor.execute(create_tables_sql)
    connection.commit()
    print("Tabele zostały utworzone pomyślnie.")

    # --- Wstawianie danych ---

    kluby = [
        ("Legia Warszawa", "Warszawa", "Stadion Wojska Polskiego", 1916),
        ("Lech Poznań", "Poznań", "Stadion Miejski", 1922),
        ("Wisła Kraków", "Kraków", "Stadion Wisły", 1906),
        ("Śląsk Wrocław", "Wrocław", "Stadion Wrocław", 1947),
        ("Górnik Zabrze", "Zabrze", "Stadion im. Ernesta Pohla", 1948),
        ("Pogoń Szczecin", "Szczecin", "Stadion Pogoni", 1948),
        ("Cracovia", "Kraków", "Stadion Cracovii", 1906),
        ("Jagiellonia Białystok", "Białystok", "Stadion Miejski", 1920),
        ("Zagłębie Lubin", "Lubin", "Stadion Zagłębia", 1945),
        ("Raków Częstochowa", "Częstochowa", "Stadion Rakowa", 1921)
    ]
    execute_values(cursor, "INSERT INTO Kluby (nazwa, miasto, stadion, rok_zalozenia) VALUES %s ON CONFLICT DO NOTHING", kluby)

    # Pobierz klub_id, aby przypisać do trenerów, piłkarzy i meczów
    cursor.execute("SELECT klub_id FROM Kluby ORDER BY klub_id ASC")
    klub_ids = [row[0] for row in cursor.fetchall()]

    trenerzy = [
        ("Jan", "Kowalski", "1965-03-10", "Polska", klub_ids[0]),
        ("Piotr", "Nowak", "1970-07-15", "Polska", klub_ids[1]),
        ("Andrzej", "Wiśniewski", "1962-12-01", "Polska", klub_ids[2]),
        ("Marek", "Kaczmarek", "1968-05-20", "Polska", klub_ids[3]),
        ("Tomasz", "Zieliński", "1975-01-30", "Polska", klub_ids[4]),
        ("Adam", "Sikora", "1963-09-10", "Polska", klub_ids[5]),
        ("Krzysztof", "Wójcik", "1972-04-14", "Polska", klub_ids[6]),
        ("Łukasz", "Kubiak", "1969-11-22", "Polska", klub_ids[7]),
        ("Dariusz", "Kowalczyk", "1971-08-08", "Polska", klub_ids[8]),
        ("Paweł", "Baran", "1967-06-16", "Polska", klub_ids[9])
    ]
    execute_values(cursor, "INSERT INTO Trenerzy (imie, nazwisko, data_urodzenia, narodowosc, klub_id) VALUES %s ON CONFLICT DO NOTHING", trenerzy)

    pilkarze = [
        ("Robert", "Lewandowski", "1988-08-21", "Polska", "Napastnik", klub_ids[0]),
        ("Kamil", "Grosicki", "1988-06-08", "Polska", "Pomocnik", klub_ids[1]),
        ("Grzegorz", "Krychowiak", "1990-01-29", "Polska", "Pomocnik", klub_ids[2]),
        ("Wojciech", "Szczęsny", "1990-04-18", "Polska", "Bramkarz", klub_ids[3]),
        ("Arkadiusz", "Milik", "1994-02-28", "Polska", "Napastnik", klub_ids[4]),
        ("Łukasz", "Piszczek", "1985-06-03", "Polska", "Obrońca", klub_ids[5]),
        ("Jakub", "Błaszczykowski", "1985-12-14", "Polska", "Pomocnik", klub_ids[6]),
        ("Bartosz", "Bereszyński", "1992-07-12", "Polska", "Obrońca", klub_ids[7]),
        ("Jan", "Bednarek", "1996-04-12", "Polska", "Obrońca", klub_ids[8]),
        ("Mateusz", "Klich", "1990-06-13", "Polska", "Pomocnik", klub_ids[9]),
        ("Szymon", "Żurkowski", "1997-08-25", "Polska", "Pomocnik", klub_ids[0]),
        ("Przemysław", "Frankowski", "1995-05-12", "Polska", "Pomocnik", klub_ids[1]),
        ("Tomasz", "Kędziora", "1994-06-11", "Polska", "Obrońca", klub_ids[2]),
        ("Michał", "Pazdan", "1987-09-19", "Polska", "Obrońca", klub_ids[3]),
        ("Sebastian", "Szymański", "1996-05-10", "Polska", "Pomocnik", klub_ids[4]),
        ("Kamil", "Jóźwiak", "1998-11-22", "Polska", "Pomocnik", klub_ids[5]),
        ("Bartosz", "Kapustka", "1996-02-20", "Polska", "Pomocnik", klub_ids[6]),
        ("Krzysztof", "Piątek", "1995-07-01", "Polska", "Napastnik", klub_ids[7]),
        ("Łukasz", "Fabiański", "1985-04-18", "Polska", "Bramkarz", klub_ids[8]),
        ("Mateusz", "Wieteska", "1997-07-04", "Polska", "Obrońca", klub_ids[9]),
        ("Damian", "Kądzior", "1992-09-16", "Polska", "Pomocnik", klub_ids[0]),
        ("Filip", "Starzyński", "1991-03-03", "Polska", "Pomocnik", klub_ids[1]),
        ("Rafał", "Augustyniak", "1991-11-12", "Polska", "Obrońca", klub_ids[2]),
        ("Łukasz", "Trałka", "1984-02-07", "Polska", "Pomocnik", klub_ids[3]),
        ("Jakub", "Kamiński", "2002-06-05", "Polska", "Pomocnik", klub_ids[4]),
        ("Szymon", "Włodarczyk", "2003-01-05", "Polska", "Napastnik", klub_ids[5]),
        ("Patryk", "Dziczek", "2000-05-01", "Polska", "Pomocnik", klub_ids[6]),
        ("Kacper", "Chodyna", "2000-12-18", "Polska", "Obrońca", klub_ids[7]),
        ("Michał", "Helik", "1995-04-09", "Polska", "Obrońca", klub_ids[8]),
        ("Bartłomiej", "Drągowski", "1997-01-19", "Polska", "Bramkarz", klub_ids[9])
    ]
    execute_values(cursor, """INSERT INTO Pilkarze 
        (imie, nazwisko, data_urodzenia, narodowosc, pozycja, klub_id) 
        VALUES %s ON CONFLICT DO NOTHING""", pilkarze)

    mecze = [
        ("2023-08-01", klub_ids[0], klub_ids[1], 2, 1, "Stadion Wojska Polskiego"),
        ("2023-08-02", klub_ids[2], klub_ids[3], 1, 1, "Stadion Wisły"),
        ("2023-08-03", klub_ids[4], klub_ids[5], 0, 3, "Stadion im. Ernesta Pohla"),
        ("2023-08-04", klub_ids[6], klub_ids[7], 2, 2, "Stadion Cracovii"),
        ("2023-08-05", klub_ids[8], klub_ids[9], 1, 0, "Stadion Zagłębia"),
        ("2023-08-06", klub_ids[1], klub_ids[0], 0, 4, "Stadion Miejski"),
        ("2023-08-07", klub_ids[3], klub_ids[2], 2, 3, "Stadion Wrocław"),
        ("2023-08-08", klub_ids[5], klub_ids[4], 1, 1, "Stadion Pogoni"),
        ("2023-08-09", klub_ids[7], klub_ids[6], 3, 0, "Stadion Miejski"),
        ("2023-08-10", klub_ids[9], klub_ids[8], 2, 2, "Stadion Rakowa")
    ]
    execute_values(cursor, """INSERT INTO Mecze 
        (data_meczu, klub_gospodarz_id, klub_gosc_id, wynik_gospodarz, wynik_gosc, stadion) 
        VALUES %s ON CONFLICT DO NOTHING""", mecze)

    connection.commit()
    print("Dane zostały dodane pomyślnie.")

except Exception as error:
    print(f"Błąd podczas tworzenia tabel lub dodawania danych: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
