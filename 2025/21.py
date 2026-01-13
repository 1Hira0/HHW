#WAP to connect Python with MySQL using database connectivity and perform the 
#following operation on data in database: Create a table in database 

import mysql.connector
def create_table():
    # Establish the database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="schoolDB"
    )
    cursor = conn.cursor()
    # Create a table
    cursor.execute("""
        CREATE TABLE Employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            department VARCHAR(100)
        )
    """)
    print("Table created successfully.")
    cursor.close()
    conn.close()
# Call the function with a sample stack
sample_stack = [10, 23, 45, 67, 80, 91, 100]
create_table()
