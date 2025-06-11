import psycopg2
from datetime import date

host = "localhost"
user = "postgres"
password = "admin"
database = "sport"

def dostepne_kluby():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT klub_id, nazwa, stadion FROM public.kluby;')
        kluby = cursor.fetchall()
        return kluby  # lista tupli (klub_id, nazwa, stadion)

    except Exception as e:
        print("Error:", e)
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def play_game(klubAid, klubBid, wynikA, wynikB, stadion):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO public.mecze 
            (klub_gospodarz_id, klub_gosc_id, wynik_gospodarz, wynik_gosc, data_meczu, stadion, rozgrywka_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """,
            (klubAid, klubBid, wynikA, wynikB, date.today(), stadion, 1)
        )
        print("klubAid="+klubAid)
        connection.commit()
        print(f"✅ Dodano mecz: {klubAid} vs {klubBid} ({wynikA}:{wynikB}) na stadionie {stadion}")

    except Exception as e:
        print("❌ Błąd:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

