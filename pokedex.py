# Practice using Python to run basic SQL queries on a local database
import mysql.connector

def sql_connect():
    return mysql.connector.connect(
        host='',
        user='',
        password='',
        database='',
        port=3306,
        auth_plugin='mysql_native_password'
    )

def create_database():
    database = sql_connect()
    db_cursor = database.cursor()
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS kanto (id int AUTO_INCREMENT PRIMARY KEY,
                      Pokemon VARCHAR(40),
                      Type VARCHAR(40)
                      )''')
    db_cursor.execute("Select * FROM kanto")

def add_pokemon():
    database = sql_connect()
    db_cursor = database.cursor()

    pokemon = input("Enter Pokemon's name: ")
    type = input("Enter its type: ")

    db_cursor.execute(f"INSERT INTO kanto (Pokemon, Type) VALUES (%s, %s)", (pokemon, type))
    database.commit()
    print(db_cursor.rowcount, "record inserted.")

def view_all_pokemon():
    database = sql_connect()
    db_cursor = database.cursor()
    db_cursor.execute("SELECT * FROM kanto")
    kanto_pokemon = db_cursor.fetchall()
    for pokemon in kanto_pokemon:
        print(pokemon)

def view_pokemon():
    database = sql_connect()
    db_cursor = database.cursor()
    id = input("Enter id of the Pokemon you wish to view: ")
    db_cursor.execute("SELECT * FROM kanto WHERE id = %s", (id,))
    pokemon = db_cursor.fetchone()
    print(pokemon)

def update_pokemon():
    database = sql_connect()
    db_cursor = database.cursor()

    id = input("Enter Id of the Pokemon to update: ")
    pokemon = input("Enter Pokemon's name: ")
    type = input("Enter its type: ")

    db_cursor.execute("UPDATE kanto SET Pokemon = %s, Type = %s WHERE id = %s", (pokemon, type, id))
    database.commit()
    print(db_cursor.rowcount, "records affected")

def delete_pokemon():
    database = sql_connect()
    db_cursor = database.cursor()

    id = input("Enter Id of the Pokemon to delete: ")

    db_cursor.execute("DELETE FROM kanto WHERE id = %s", (id,))
    database.commit()
    print(db_cursor.rowcount, "record(s) affected")

def reset_autoincrement():
    '''Reset the autoincrement after a deletion of a record'''
    database = sql_connect()
    db_cursor = database.cursor()

    new_autoincrement = input("Enter the value that autoincrement should reset to: ")

    db_cursor.execute("ALTER TABLE kanto AUTO_INCREMENT = %s", (new_autoincrement,))
    database.commit()

def main():
    create_database()
    while True:
        print("1. Add Pokemon \n2. View All Pokemon \n3. View Single Pokemon \n4. Update Pokemon \n5. Delete Pokemon \n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_pokemon()
        elif choice == "2":
            view_all_pokemon()
        elif choice == "3":
            view_pokemon()
        elif choice == "4":
            update_pokemon()
        elif choice == "5":
            delete_pokemon()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice...")

if __name__ == "__main__":
    main()