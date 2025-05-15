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

    courses = ["matematyka" , "fizyka" , "chemia" , "polski" , "angielski" , "przyroda" , "informatyka" , "wf" , "niemiecki" , "wdz"]

    for i in range(10):
        insert_query = "INSERT INTO public.courses (course_id, course_name, credits) VALUES (%s, %s, %s);"
        id= i +1
        name = courses[i]
        credits = i+1
        cursor.execute(insert_query, (id, name, credits))
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
