import psycopg2

# Database connection parameters
host = "localhost"
database = "schooldb"
user = "postgres"
password = "admin"

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
    for i in range(100):
        id = i
        name = f"user {i}" 
        email= f"user{i}@email.pl"
        cursor.execute(update , ( name , email , id))

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
