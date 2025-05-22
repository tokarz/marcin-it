import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

host = "localhost"
user = "postgres"
password = "admin"

try:
    # Połącz się z bazą 'postgres', NIE z 'sport'
    connection = psycopg2.connect(
        host=host,
        database="postgres",
        user=user,
        password=password
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # Sprawdź, czy baza 'sport' istnieje
    cursor.execute("SELECT 1 FROM pg_database WHERE datname='sport'")
    exists = cursor.fetchone()

    if exists:
        # Zakończ aktywne połączenia z bazą 'sport'
        cursor.execute("""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = 'sport' AND pid <> pg_backend_pid();
        """)

        # Usuń bazę danych
        cursor.execute(sql.SQL("DROP DATABASE sport"))
        print("Baza danych 'sport' została usunięta.")
    else:
        print("Baza danych 'sport' nie istnieje.")

except Exception as error:
    print(f"Błąd podczas usuwania bazy danych: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()