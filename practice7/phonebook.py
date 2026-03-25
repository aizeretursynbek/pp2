import psycopg2
import csv
from config import load_config

config=load_config()
conn=psycopg2.connect(**config)
cur=conn.cursor()
cur.execute("DROP TABLE IF EXISTS phonebook;")
cur.execute("CREATE TABLE phonebook (id SERIAL PRIMARY KEY, name VARCHAR(100), phone VARCHAR(100));")
conn.commit()


def insert_from_csv():
    with open("contacts.csv","r") as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name,phone) VALUES (%s,%s)",row)
    conn.commit()
    print("Added succesfully from csv file")


def insert_from_console():
    name= input("Enter the name: ")
    phone=input("Enter the phone: ")
    cur.execute("INSERT INTO phonebook(name,phone) VALUES (%s,%s)", (name,phone))
    conn.commit()


def update_table():
    cur.execute("UPDATE phonebook SET phone='+7' || SUBSTRING(phone FROM 2) WHERE phone LIKE '8%'")
    conn.commit()
    print("Data has changed succesfully")


def search_contacts():
    print("1.View all contacts\n2.Search with name.\n3.Search by phone prefix.")
    choice=input("Enter yout choice: ")
    if choice =="1":
        cur.execute("SELECT * FROM phonebook")
        rows=cur.fetchall()
    elif choice=="2":
        name= input("Enter the name for search: ")
        cur.execute("SELECT * FROM phonebook WHERE name= %s", (name,))
        rows=cur.fetchall()
    elif choice=="3":
        pref=input("Enter the prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (pref +'%',))
        rows=cur.fetchall()
    else:
        print("Can not search!")
        return
    
    if rows:
        for row in rows:
            print(f"ID:{row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("Nothing found.")


def delete_contacts():
    name=input("Enter the name you want to delete: ")
    cur.execute(" DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()
    if cur.rowcount==0:
        print("Nothing to delete")
    else:
        print("Deleted successfully")


try:
    while True:
        print("1.Insert from csv\n2.Insert from console\n3.Update the data\n4.search contacts\n5.Delete contacts\n0.exit")
        choice=input("Enter your action: ")
        if choice=="1":
            insert_from_csv()
        elif choice=="2":
            insert_from_console()
        elif choice=="3":
            update_table()
        elif choice=="4":
            search_contacts()
        elif choice=="5":
            delete_contacts()
        elif choice=="0":
            break
        else:
            print("Wrong choice")
except Exception as e:
    print("Error:", e)
finally:
    cur.close()
    conn.close()
    print("Connection closed")