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


###############

def get_trener_klubu(klub_id):
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

