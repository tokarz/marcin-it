import psycopg2

host = "localhost"
user = "postgres"
password = "admin"

def get_kluby():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT klub_id , nazwa FROM "kluby";')
        kluby = cursor.fetchall()
        return kluby
        

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def get_trenerzy():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT imie , nazwisko FROM "trenerzy";')
        trenerzy = cursor.fetchall()
        return trenerzy

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def get_pilkarze():
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


def get_rozgrywki():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT nazwa FROM "rozgrywki";')
        rozgrywki = cursor.fetchall()
        return rozgrywki

    except Exception as e:
        print("Error:", e)


def get_historie():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT historie FROM "historia";')
        historie = cursor.fetchall()
        return historie

    except Exception as e:
        print("Error:", e)


def get_mecze():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "mecze";')
        mecze = cursor.fetchall()
        return mecze

    except Exception as e:
        print("Error:", e)

def get_statystyki():
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute('SELECT szybkosc , sila, drybling , obrona , podania , ogolna_ocena FROM "statystyki";')
        statystyki = cursor.fetchall()
        return statystyki

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



###############

def get_club_trener(klub_id):
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f'SELECT imie , nazwisko FROM "trenerzy" WHERE klub_id={klub_id}')
        trenerzy = cursor.fetchall()
        return trenerzy

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def get_history_of_club(klub_id):
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f'SELECT historia FROM "historia" WHERE klub_id={klub_id}')
        trenerzy = cursor.fetchall()
        return trenerzy

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def get_statistic_of_player(pilkarz_id):
    try:
        connection = psycopg2.connect(
            host=host,
            database='sport',
            user=user,
            password=password
        )
        cursor = connection.cursor()
        sql = f"""
            SELECT p.imie, p.nazwisko, p.data_urodzenia, p.narodowosc, p.pozycja,
                   s.szybkosc, s.sila, s.drybling, s.obrona, s.podania, s.ogolna_ocena
            FROM pilkarze p
            JOIN statystyki s ON p.pilkarz_id = s.pilkarz_id
            WHERE p.pilkarz_id = {pilkarz_id};
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
