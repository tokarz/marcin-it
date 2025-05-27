import psycopg2

host = "localhost"
user = "postgres"
password = "admin"
database = "sport"

def wypisz_mecze():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                m.mecz_id, 
                k1.nazwa AS gospodarz, 
                k2.nazwa AS gosc, 
                m.wynik_gospodarz, 
                m.wynik_gosc, 
                m.data_meczu
            FROM 
                public.mecze m
            JOIN public.kluby k1 ON m.klub_gospodarz_id = k1.klub_id
            JOIN public.kluby k2 ON m.klub_gosc_id = k2.klub_id
            ORDER BY m.mecz_id;
        """)
        wyniki = cursor.fetchall()

        print("\n Lista wszystkich meczów:")
        for mecz in wyniki:
            print(f"{mecz[0]}. {mecz[1]} vs {mecz[2]} -- wynik: {mecz[3]}:{mecz[4]} -- data: {mecz[5]}")
        
        return [m[0] for m in wyniki]  # zwraca listę ID meczów

    except Exception as e:
        print("❌ Błąd podczas pobierania meczów:", e)
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def aktualizuj_mecz(mecz_id, nowy_wynik_gosp, nowy_wynik_gosc):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE public.mecze
            SET wynik_gospodarz = %s,
                wynik_gosc = %s
            WHERE mecz_id = %s;
        """, (nowy_wynik_gosp, nowy_wynik_gosc, mecz_id))
        connection.commit()
        print(f"✅ Udalo sie zaktualizowac mecz o ID =  {mecz_id}.")

    except Exception as e:
        print("❌ Błąd podczas aktualizacji:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# -----------------------------------
# Główna logika programu

dostepne_id = wypisz_mecze()

if not dostepne_id:
    print("Brak meczów do aktualizacji.")
else:
    try:
        mecz_id = int(input("\nPodaj ID meczu do aktualizacji -> "))
        if mecz_id not in dostepne_id:
            print("❌ Nieprawidłowy ID meczu.")
        else:
            nowy_wynik_gosp = int(input("Podaj nowy wynik gospodarza -> "))
            nowy_wynik_gosc = int(input("Podaj nowy wynik gościa -> "))

            if not (0 <= nowy_wynik_gosp <= 50 and 0 <= nowy_wynik_gosc <= 50):
                print("❌Wynik musi mieścić się w przedziale 0-50!!!.❌")
            else:
                aktualizuj_mecz(mecz_id, nowy_wynik_gosp, nowy_wynik_gosc)

    except ValueError:
        print("❌ Wprowadzono nieprawidłowe dane liczbowe.")