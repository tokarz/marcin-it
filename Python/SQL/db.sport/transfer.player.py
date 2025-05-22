import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

host = "localhost"
user = "postgres"
password = "admin"

def dostepne_kluby():
    try:
    # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )

        cursor = connection.cursor()

        cursor.execute('select klub_id from "kluby";')
        kluby = cursor.fetchall()
        return kluby[0]

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def dostepni_pilkarze():
    try:
    # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )

        cursor = connection.cursor()

        cursor.execute('select pilkarz_id from "pilkarze";')
        pilkarze = cursor.fetchall()
        return pilkarze

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()





def transfer_player(klub_id , pilkarz_id):
    try:
    # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=host,
            database="sport",
            user=user,
            password=password
        )

    # Create a cursor object
        cursor = connection.cursor()
        cursor.execute(f'UPDATE public.pilkarze SET  klub_id={klub_id} WHERE pilkarz_id = {pilkarz_id};')

        connection.commit()

    except Exception as e:
        print("Error:", e)
        connection.rollback()

    finally:
    # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

klub = input("Podaj klub")
kluby = dostepne_kluby()

for k in kluby:
    print(k)
pilkarz= input("Jaki pilkarz")
pilkarze = dostepni_pilkarze()
if klub in kluby:
    if pilkarz in pilkarze:
        transfer_player(klub , pilkarz)
    else:
        print("Nie ma takiego pilkarza! Dostepni pilkarze to :")
        print(pilkarze)
else :
    print("Nie ma takiego klubu! Dostępne kluby to :")
    print (kluby)
