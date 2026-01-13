#WAP to connect Python with MySQL using database connectivity and perform the 
#following operation on data in database: Delete record from the table 

import mysql.connector
def delete_record(employee_id):
    # Establish the database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="schoolDB"
    )
    cursor = conn.cursor()
    # Delete a record from the Employees table
    cursor.execute("DELETE FROM Employees WHERE id = %s", (employee_id,))
    conn.commit()
    print("Record deleted successfully.")
    cursor.close()
    conn.close()
    