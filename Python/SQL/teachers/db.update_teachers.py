import psycopg2

# Database connection parameters
host = "localhost"
database = "schooldb"
user = "postgres"
password = "admin"


def update_teachers(where):
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
        update = 'UPDATE public.teachers SET  name=%s, email=%s WHERE teacher_id=%s' 
        cursor.execute(f'select * from "teachers" WHERE {where}')

    # Fetch and print the result
        rows = cursor.fetchall()

    # Print all rows
        for row in rows:
            teacher_id = row[0]  #teacher_id
            name = f"teacher {teacher_id}" 
            email= f"teacher{teacher_id}@interia.pl"
            cursor.execute(update , ( name , email , teacher_id))

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


update_teachers("teachers.teacher_id < 10")