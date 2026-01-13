#WAP to connect Python with MySQL using database connectivity and perform the 
#following operation on data in database: Update record in the table

import mysql.connector
def update_record(employee_id, name=None, age=None, department=None):
    # Establish the database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="schoolDB"
    )
    cursor = conn.cursor()
    # Prepare the update statement
    update_fields = []
    if name is not None:
        update_fields.append("name = %s")
    if age is not None:
        update_fields.append("age = %s")
    if department is not None:
        update_fields.append("department = %s")
    update_statement = "UPDATE Employees SET " + ", ".join(update_fields) + " WHERE id = %s"
    values = [val for val in (name, age, department) if val is not None]
    values.append(employee_id)
    # Execute the update statement
    cursor.execute(update_statement, tuple(values))
    conn.commit()
    print("Record updated successfully.")
    cursor.close()
    conn.close()
    