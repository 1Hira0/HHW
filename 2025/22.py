#WAP to connect Python with MySQL using database connectivity and perform the 
#following operation on data in database: Insert record in the table 

import mysql.connector
def insert_record(name, age, department):
    # Establish the database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="schoolDB"
    )
    cursor = conn.cursor()
    # Insert a record into the Employees table
    cursor.execute(f"""
        INSERT INTO Employees (name, age, department)
        VALUES ({name}, {age}, {department})
    """, (name, age, department))
    conn.commit()
    print("Record inserted successfully.")
    cursor.close()
    conn.close()
