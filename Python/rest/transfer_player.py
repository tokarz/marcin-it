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
        cursor.execute('SELECT imie , nazwisko FROM "pilkarze";')
        pilkarze = cursor.fetchall()
        return pilkarze

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
