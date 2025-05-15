import psycopg2

# Database connection parameters
host = "localhost"
database = "schooldb"
user = "postgres"
password = "admin"


def show_enrollments_for_teacher(teacher_id):
    try:
    # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

    # Create a cursor object
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM public.enrollments JOIN students ON enrollments.student_id = students.student_id WHERE teacher_id = {teacher_id}')

    # Fetch and print the result
        rows = cursor.fetchall()

            # Print all rows
        for row in rows:
            print("teacher:", row[4],"student",row[6] ,  "email:", row[7])

    except Exception as e:
        print("Error:", e)
        connection.rollback()

    finally:
    # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()



def add_enrollments():
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Pobranie danych z tabel
        cursor.execute('SELECT * FROM "teachers";')
        teachers = cursor.fetchall()
        cursor.execute('SELECT * FROM "courses";')
        courses = cursor.fetchall()
        cursor.execute('SELECT * FROM "students";')
        students = cursor.fetchall()

        # 1. Dla każdego nauczyciela jest jeden kurs i 10 studentów 
        # 2. Musimy zrobić pętlę dla każdego nauczyciela i zrobić 10 INSERT-ów do enrollments 
        currentIndex = 0
        date = '2025-05-15'

        for teacher in teachers:
            teacherId = teacher[0]
            courseId = courses[0][0]

            for i in range(10):
                if currentIndex >= len(students):
                    print("Za mało studentów w bazie danych!")
                    break

                studentId = students[currentIndex][0]
                insert_query = """
                INSERT INTO public.enrollments 
                (enrollment_id, student_id, course_id, enrollment_date, teacher_id) 
                VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(insert_query, (currentIndex, studentId, courseId, date, teacherId))
                currentIndex += 1
                print(f"Enrollment {currentIndex} dodany.")

        # Zatwierdzenie transakcji
        connection.commit()

    except Exception as e:
        print("Błąd:", e)
        connection.rollback()

    finally:
        # Zamknięcie kursora i połączenia
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

show_enrollments_for_teacher(1)