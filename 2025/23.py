#WAP to connect Python with MySQL using database connectivity and perform the 
#following operation on data in database: Fetch records from the table using fetchone( ), 
#fetchall() and fetchmany( )

import mysql.connector
def fetch_records():
    # Establish the database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="schoolDB"
    )
    cursor = conn.cursor()
    # Fetch all records from the Employees table
    cursor.execute("SELECT * FROM Employees")
    print("Fetching one record:")
    record = cursor.fetchone()
    print(record)
    print("\nFetching next three records:")
    records = cursor.fetchmany(3)
    for rec in records:
        print(rec)
    print("\nFetching all remaining records:")
    records = cursor.fetchall()
    for rec in records:
        print(rec)
    cursor.close()
    conn.close()