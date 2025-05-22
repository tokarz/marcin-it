import psycopg2

host = "localhost"
user = "postgres"
password = "admin"

def dostepne_kluby():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT klub_id FROM "kluby";')
        kluby = cursor.fetchall()
        return [k[0] for k in kluby]  # <-- teraz to [1, 2, 3]

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def dostepni_trenerzy():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT trener_id FROM "trenerzy";')
        trenerzy = cursor.fetchall()
        return [p[0] for p in trenerzy]  

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def transfer_player(klub_id, trener_id):
    try:
        connection = psycopg2.connect(
            host=host,
            database="sport",
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE public.trenerzy SET klub_id = {klub_id} WHERE trener_id = {trener_id};'
        )
        connection.commit()
        print(f"Trener {trener_id} zmienil klub na {klub_id}.")

    except Exception as e:
        print("Error:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# -------------------------------
# Główna część programu

kluby = dostepne_kluby()
print("Dostępne kluby:", kluby)
klub = int(input("Podaj ID klubu: "))

trenerzy = dostepni_trenerzy()
print("Dostępni trenerzy:", trenerzy)
trener = int(input("Podaj ID trenera: "))

if klub in kluby:
    if trener in trenerzy:
        transfer_player(klub, trener)
    else:
        print("Nie ma takiego trenera!")
else:
    print("Nie ma takiego klubu!")