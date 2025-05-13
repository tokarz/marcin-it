import psycopg2

# Database connection parameters
host = "localhost"
database = "schooldb"
user = "postgres"
password = "admin"


def update_students(where):
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
        update = 'UPDATE public.students SET  name=%s, email=%s WHERE student_id=%s' 
        cursor.execute(f'select * from "students" WHERE {where}')

    # Fetch and print the result
        rows = cursor.fetchall()

    # Print all rows
        for row in rows:
            sudent_id = row[0]  # student_id
            name = f"user {sudent_id}" 
            email= f"user{sudent_id}@email.ru"
            cursor.execute(update , ( name , email , sudent_id))

    # Fetch and print the result
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


update_students("students.student_id > 50")