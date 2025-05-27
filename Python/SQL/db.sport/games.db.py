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
            (klub_gospodarz_id, klub_gosc_id, wynik_gospodarz, wynik_gosc, data_meczu, stadion) 
            VALUES (%s, %s, %s, %s, %s, %s);
            """,
            (klubAid, klubBid, wynikA, wynikB, date.today(), stadion)
        )
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

# -------------------------------
# Główna część programu

kluby = dostepne_kluby()
print("Dostępne kluby i ich stadiony:")
for klub_id, nazwa, stadion in kluby:
    print(f"{klub_id}: {nazwa} (stadion: {stadion})")

try:
    klubA = int(input("\nPodaj ID klubu gospodarza: "))
    klubB = int(input("Podaj ID klubu gościa: "))

    klub_ids = [k[0] for k in kluby]

    if klubA not in klub_ids or klubB not in klub_ids:
        print("❌ Nieprawidłowy ID klubu.")
    elif klubA == klubB:
        print("❌ Klub nie może grać sam ze sobą.")
    else:
        wynikA = int(input("Podaj wynik klubu gospodarza: "))
        wynikB = int(input("Podaj wynik klubu gościa: "))
        # Pobierz stadion gospodarza z listy
        stadion = next((k[2] for k in kluby if k[0] == klubA), None)
        if stadion is None:
            print("❌ Nie znaleziono stadionu dla gospodarza!")
        else:
            play_game(klubA, klubB, wynikA, wynikB, stadion)

except ValueError:
    print("❌ Wprowadzono nieprawidłowe dane.")
