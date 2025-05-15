import psycopg2

# Database connection parameters
host = "localhost"
database = "schooldb"
user = "postgres"
password = "admin"


def delete_all_students():
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

        # Execute a simple SQL query
        cursor.execute("DELETE FROM public.students;")

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

def delete_student(where):
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
        delete = f'DELETE FROM public.students WHERE {where}'
        cursor.execute(delete)

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

delete_all_students()