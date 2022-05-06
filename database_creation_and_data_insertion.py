
# imprted sqlite3 library for database purpose
import sqlite3

# function defined to create subscriber and newsletter table in the database
def create_subscriber_and_newsletter_table():
    try:
        # connecting to the databse
        sqliteConnection = sqlite3.connect('newsletter.db')
        # running query to create Subscriber and Newsletter table
        q1 = '''CREATE TABLE Subscriber (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email text NOT NULL UNIQUE);'''
        q2 = '''CREATE TABLE Newsletter (
                id INTEGER PRIMARY KEY,
                head TEXT NOT NULL,
                message text NOT NULL);'''
        cursor = sqliteConnection.cursor()

        # executing the query
        cursor.execute(q1)
        cursor.execute(q2)
        sqliteConnection.commit()
        print("Subscriber and Newsletter Table Created Successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# function defined to insert the data into the Subscriber table
def Subscriber_insert(name, email):
    try:
        # connecting to the database
        sqliteConnection = sqlite3.connect('newsletter.db')
        cursor = sqliteConnection.cursor()

        # creating insert query statement
        q1 = """INSERT INTO Subscriber (name, email) VALUES (?, ?)"""

        cursor.execute(q1,(name,email))
        print("Data Inserted to Subscriber Table Successfully.")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# function defined to insert the data into the Newsletter table
def Newsletter_insert(head1, message):
    try:
        # connecting to the database table
        sqliteConnection = sqlite3.connect('newsletter.db')
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")

        # creating query to insert the data into the Newsletter table
        sqlite_insert_query = """INSERT INTO Newsletter (head, message) VALUES (?, ?)"""

        cursor.execute(sqlite_insert_query,(head1,message))
        print("Data Inserted to Newsletter Table Successfully.")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# running the program in command line
flag = True
while flag:
    # option for different task
    print("\n1.) To Create Database Table.\n2.) To Insert Data into Subscriber Table.\n3.) To Insert Data into Newsletter Table\n0.) To Exit from the Service.")
    option = input()
    if option == '1':
        create_subscriber_and_newsletter_table()
    elif option == '2':
        name = input("Name of Subscriber: ")
        email = input("Email Id of Subscriber: ")
        Subscriber_insert(name, email)
    elif option == '3':
        head1 = input("Message Heading: ")
        message = input("Message: ")
        Newsletter_insert(head1, message)
    else :
        flag = False

    if(flag == False):
        break