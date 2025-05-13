import psycopg2

# Database connection parameters
host = "localhost"
database = "TestDB"
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
    cursor.execute('select * from "Students" join "Klasa" on "Klasa"."Id" = "Students"."Klasa_ID";')

    # Fetch and print the result
    rows = cursor.fetchall()

    # Print all rows
    for row in rows:
        print("Name:", row[0], "Klasa_ID:", row[1])

except Exception as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
