import psycopg2

host = "localhost"
user = "postgres"
password = "admin"


def show_all_coach():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT trenerzy.imie , trenerzy.nazwisko FROM trenerzy;")
        trenerzy = cursor.fetchall()
        return [p[0]+p[1] for p in trenerzy]  

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



def show_coach_players(imie_trenera , nazwisko_trenera):
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT pilkarze.imie , pilkarze.nazwisko FROM public.pilkarze JOIN kluby ON pilkarze.klub_id = kluby.klub_id JOIN trenerzy ON trenerzy.klub_id = kluby.klub_id WHERE trenerzy.imie = '{imie_trenera}' AND trenerzy.nazwisko = '{nazwisko_trenera}';")
        players = cursor.fetchall()
        print(players)

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

trenerzy = show_all_coach()
print("Dostępni trenerzy:", trenerzy)
coach_name = input("Podaj Imie : ")
coach_lastName = input("Podaj nazwisko : ")
imie_i_nazwisko = coach_name + coach_lastName
if imie_i_nazwisko in trenerzy:
    show_coach_players(coach_name , coach_lastName)
else : 
    print("Nie ma takiego trenera : " + imie_i_nazwisko)


