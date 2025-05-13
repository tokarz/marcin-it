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

    # Execute a simple SQL query
    #cursor.execute("INSERT INTO public.students(student_id, name, email) VALUES (5, 'daniel daniel' , 'daniel@gmail.com' );")
    for i in range(100):
        insert_query = "INSERT INTO public.students(student_id, name, email) VALUES (%s , %s, %s);"
        id= i
        name = f"user {i}" 
        email= f"user{i}@email.com"
        cursor.execute(insert_query, (id, name, email))
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
