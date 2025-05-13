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
    cursor.execute('select * from "students";')

    # Fetch and print the result
    rows = cursor.fetchall()

    # Print all rows
    for row in rows:
        print("Name:", row[1], "email:", row[2])

except Exception as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
