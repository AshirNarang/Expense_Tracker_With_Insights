import mysql.connector 
import time
import config

def connect():
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        
    )

def setup():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS expence_tracker")
    cursor.execute("USE expence_tracker")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        category VARCHAR(50),
        amount FLOAT,
        description VARCHAR(200)
        )
    """)

    conn.commit()
    conn.close()

def insert_expense(date,category,amt,desc):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    query = "INSERT INTO expenses (date,category,amount,description) VALUES(%s,%s,%s,%s)"
    data = (date,category,amt,desc)
    cursor.execute(query,data)
    print("Expense Added Successfully")
    time.sleep(5)

    conn.commit()
    conn.close()

def get_expense():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_details(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    query = "SELECT * FROM expenses WHERE id=%s"
    cursor.execute(query,(id,))
    row = cursor.fetchall()
    conn.close()
    return row

def delete_details(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    query = "DELETE FROM expenses WHERE id=%s"
    cursor.execute(query,(id,))
    conn.commit()
    conn.close()

def search_details_by_ID(search):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    query = "SELECT * FROM expenses WHERE id=%s"
    cursor.execute(query,(search,))
    details = cursor.fetchall()
    conn.close()
    return details

def search_details_by_category(search):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    query = "SELECT * FROM expenses WHERE category=%s"
    cursor.execute(query,(search,))
    details = cursor.fetchall()
    conn.close()
    return details

def search_details_by_amount(search):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    query = "SELECT * FROM expenses WHERE amount=%s"
    cursor.execute(query,(search,))
    details = cursor.fetchall()
    conn.close()
    return details

def update_details(id,date,category,amt,desc):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("USE expence_tracker")
    query = "UPDATE expenses SET date=%s , category=%s , amount=%s , description=%s WHERE id=%s"
    data = (date,category,amt,desc,id)
    cursor.execute(query,data)
    conn.commit()
    conn.close()


