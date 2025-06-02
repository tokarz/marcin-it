import psycopg2
from datetime import date
from csv_reader import get_csv_rows

host = "localhost"
user = "postgres"
password = "admin"
database = "sport"

def import_games():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        mecze = get_csv_rows('sezon-ek-2024-2025.csv')
        print(f"wczytane mecze={mecze}")
        for mecz in mecze:
            print(f"aktualny mecz={mecz[0]}")

            sql = f"""
                INSERT INTO public.mecze 
                (klub_gospodarz_id, klub_gosc_id, wynik_gospodarz, wynik_gosc, data_meczu, stadion, rozgrywka_id) 
                VALUES ({int(mecz[0])}, {int(mecz[1])}, {int(mecz[2])}, {int(mecz[3])}, '{mecz[4]}', '{mecz[5]}', {int(mecz[6])});
            """.replace("\n", "")
            print(sql)
            cursor.execute(sql)
            print(f"✅ Dodano mecz: {mecz[0]} vs {mecz[1]} ({mecz[2]}:{mecz[3]}) na stadionie {mecz[5]}")

        connection.commit()

    except Exception as e:
        print("❌ Błąd:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def import_teams():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        druzyny = get_csv_rows('druzyny.csv')
        print(f"wczytane druzyny={druzyny}")
        for druzyna in druzyny:
            print(f"aktualna druzyna={druzyna[0]}")

            sql = f"""
                INSERT INTO public.kluby 
                (nazwa, miasto, stadion, rok_zalozenia) 
                VALUES ('{druzyna[0]}', '{druzyna[1]}', '{druzyna[2]}', '{druzyna[3]}');
            """.replace("\n", "")
            print(sql)
            cursor.execute(sql)
            print(f"✅ Dodano druzyne: {druzyna[0]}, {druzyna[1]}, {druzyna[2]}, {druzyna[3]}")

        connection.commit()

    except Exception as e:
        print("❌ Błąd:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def import_coach():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        trenerzy = get_csv_rows('coach.csv')
        print(f"wczytani trenerzy={trenerzy}")
        for trener in trenerzy:
            print(f"aktualny trener={trener[0]}")

            sql = f"""
                INSERT INTO public.trenerzy
                (imie, nazwisko, data_urodzenia, narodowosc, klub_id) 
                VALUES ('{trener[0]}', '{trener[1]}', '{trener[2]}', '{trener[3]}', {int(trener[4])});
            """.replace("\n", "")
            print(sql)
            cursor.execute(sql)
            print(f"✅ Dodano trenera: {trener[0]}, {trener[1]}, {trener[2]}, {trener[3]}")

        connection.commit()

    except Exception as e:
        print("❌ Błąd:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def import_rozgrywki():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        rozgrywki = get_csv_rows('rozgrywki.csv')
        print(f"wczytane rozgrywki={rozgrywki}")
        for rozgrywka in rozgrywki:
            print(f"aktualna rozgrywka={rozgrywka[0]}")

            sql = f"""
                INSERT INTO public.rozgrywki
                (nazwa) 
                VALUES ('{rozgrywka[0]}');
            """.replace("\n", "")
            print(sql)
            cursor.execute(sql)
            print(f"✅ Dodano rozgrywke: {rozgrywka[0]}")

        connection.commit()

    except Exception as e:
        print("❌ Błąd:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def import_historia():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        historie = get_csv_rows('historie.csv')
        print(f"wczytane historie={historie}")
        for historia in historie:
            print(f"aktualna historia={historia[0]}")

            sql = f"""
                INSERT INTO public.historia
                (historia, klub_id) 
                VALUES ('{historia[0]}', {int(historia[1])});
            """.replace("\n", "")
            print(sql)
            cursor.execute(sql)
            print(f"✅ Dodano historie: {historia[0]}")

        connection.commit()

    except Exception as e:
        print("❌ Błąd:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def import_players():
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        pilkarze = get_csv_rows('pilkarze.csv')
        print(f"wczytani gracze={pilkarze}")
        for pilkarz in pilkarze:
            print(f"aktualny gracz={pilkarz[0]}")

            sql = f"""
                INSERT INTO public.pilkarze
                (imie, nazwisko, data_urodzenia, narodowosc, pozycja, klub_id) 
                VALUES ('{pilkarz[0]}', '{pilkarz[1]}', '{pilkarz[2]}', '{pilkarz[3]}', '{pilkarz[4]}', {int(pilkarz[5])});
            """.replace("\n", "")
            print(sql)
            cursor.execute(sql)
            print(f"✅ Dodano pilkarza: {pilkarz[0]}")

        connection.commit()

    except Exception as e:
        print("❌ Błąd:", e)
        connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Wywołanie importów
# import_games()
# import_teams()
# import_coach()
# import_rozgrywki()
# import_historia()
import_players()
