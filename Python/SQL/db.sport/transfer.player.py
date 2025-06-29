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

def dostepni_pilkarze():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT pilkarz_id FROM "pilkarze";')
        pilkarze = cursor.fetchall()
        return [p[0] for p in pilkarze]  # <-- teraz to [10, 11, 12]

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def transfer_player(klub_id, pilkarz_id):
    try:
        connection = psycopg2.connect(
            host=host,
            database="sport",
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE public.pilkarze SET klub_id = {klub_id} WHERE pilkarz_id = {pilkarz_id};'
        )
        connection.commit()
        print(f"Piłkarz {pilkarz_id} został przeniesiony do klubu {klub_id}.")

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

pilkarze = dostepni_pilkarze()
print("Dostępni piłkarze:", pilkarze)
pilkarz = int(input("Podaj ID piłkarza: "))

if klub in kluby:
    if pilkarz in pilkarze:
        transfer_player(klub, pilkarz)
    else:
        print("Nie ma takiego piłkarza!")
else:
    print("Nie ma takiego klubu!")